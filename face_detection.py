import cv2
class face:
    def __init__(self):
        self.cascade=cv2.CascadeClassifier('faces.xml')
        self.x=None
        self.y=None
        self.w=None
        self.h=None

    def detectFace(self,img):
        cropped=None
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.cascade.detectMultiScale(grey,1.3,5)
        for (self.x,self.y,self.w,self.h) in faces:
            cropped=img[self.y:self.y+self.h,self.x:self.x+self.w]
        return cropped,self.x,self.y,self.w,self.h
