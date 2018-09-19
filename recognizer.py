import cv2
from align import Allign
from face_detection import face

all=Allign()
fd=face()
cap=cv2.VideoCapture(0)
while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    detected=fd.detectFace(frame)
    if(detected is not None):
        faces=all.Al(detected)
        cv2.imshow('frame',faces)
    cv2.waitKey(1)
