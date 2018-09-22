import cv2
from face_detection import face
from keras.models import load_model
import numpy as np
from embedding import emb


e=emb()
fd=face()
model=load_model('face_reco.MODEL')
cap=cv2.VideoCapture(1)
while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    detected=fd.detectFace(frame)

    if(detected is not None):
        f=detected
        detected=cv2.resize(detected,(160,160))
        detected=detected.astype('float')/255.0
        detected=np.expand_dims(detected,axis=0)
        feed=e.calculate(detected)
        feed=np.expand_dims(feed,axis=0)
        prediction=model.predict(feed)[0]
        result=np.argmax(prediction)
        cv2.putText(frame,str(result),(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
        cv2.imshow('frame',f)
    cv2.imshow('dd',frame)
    if(cv2.waitKey(1) & 0XFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
