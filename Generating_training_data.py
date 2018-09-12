import cv2
import numpy as np
import os
pic_no=0
print('enter the name of the person for enrollment')
name=input()
os.makedirs(name)
fa=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
ret=True
while ret:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=fa.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cropped=frame[y:y+h,x:x+w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2,cv2.LINE_AA)
        pic_no=pic_no+1
        cv2.imwrite(name+'/'+str(pic_no)+'.jpg',cropped)
    cv2.imshow('frame',frame)
    cv2.waitKey(100)

    if(pic_no>50):
    	break


cap.release()
cv2.destroyAllWindows()
