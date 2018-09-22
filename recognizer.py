import cv2
from face_detection import face
from keras.models import load_model
import numpy as np
from embedding import emb
from retreive_pymongo_data import database


label=None
a={"satinder":0,"sagat":0,"mandeep":0}


data=database()
e=emb()
fd=face()

print('attendance till now is ')
data.view()

model=load_model('face_reco.MODEL')
cap=cv2.VideoCapture(1)
ret=True

while ret:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    detected,x,y,w,h=fd.detectFace(frame)

    if(detected is not None):
        f=detected
        detected=cv2.resize(detected,(160,160))
        detected=detected.astype('float')/255.0
        detected=np.expand_dims(detected,axis=0)
        feed=e.calculate(detected)
        feed=np.expand_dims(feed,axis=0)
        prediction=model.predict(feed)[0]

        result=int(np.argmax(prediction))
        if(result==0):
            label="satinder"
            if(a[label]==0):
                data.update(label)
            a[label]=1


        elif(result==1):
            label="sagat"
            if(a[label]==0):
                data.update(label)
            a[label]=1


        elif(result==2):
            label="mandeep"
            if(a[label]==0):
                data.update(label)
            a[label]=1


        #data.update(label)
        cv2.putText(frame,label,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        if(a[label]==1):
            cv2.putText(frame,"your attendance is complete",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(252,160,39),3)
        cv2.imshow('onlyFace',f)
    cv2.imshow('frame',frame)
    if(cv2.waitKey(1) & 0XFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
data.export_csv()
