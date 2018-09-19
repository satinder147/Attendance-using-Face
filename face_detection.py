import cv2

class face:
    def __init__(self):
        self.cascade=cv2.CascadeClassifier('faces.xml')
    def detectFace(self,img):
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.cascade.detectMultiScale(grey,1.3,5)
        for (x,y,w,h) in faces:
            return img[y:y+h,x:x+w]
