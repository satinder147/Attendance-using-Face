import cv2
import dlib

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
        for i in range(68):
            cv2.circle(faces,(features.part(i).x,features.part(i).y),2,(255,0,0),-2)
            cv2.putText(faces,)
        return faces
