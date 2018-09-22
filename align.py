import cv2
import dlib
import numpy as np
class Allign:
    def __init__(self):
        self.pred=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    def tup(self,a,b,c,d):
        return dlib.rectangle(int(a),int(b),int(c),int(d))
    def Al(self,faces):
        w,h=faces.shape[:2]
        grey=cv2.cvtColor(faces,cv2.COLOR_BGR2GRAY)
        d=self.tup(0,0,w,h)
        features=self.pred(grey,d)


        first_x=int((features.part(36).x+features.part(39).x)/2)
        first_y=int((features.part(36).y+features.part(39).y)/2)
        second_x=int((features.part(42).x+features.part(45).x)/2)
        second_y=int((features.part(42).y+features.part(45).y)/2)
        cv2.line(faces,(first_x,first_y),(second_x,second_y),(255,0,0),2)
        dx=first_x-second_x
        dy=first_y-second_y
        angle=np.degrees(np.arctan2(dy,dx))-180
        print(angle)
        #for i in range(68):
            #cv2.circle(faces,(features.part(i).x,features.part(i).y),2,(255,0,0),-2)
            #cv2.putText(faces,str(i),(features.part(i).x,features.part(i).y),cv2.FONT_HERSHEY_SIMPLEX,0.25,(0,255,0),1)
        return faces,angle
