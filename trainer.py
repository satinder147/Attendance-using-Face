from modelArch import DenseArchs
import cv2
import numpy as np
import os
from embedding import emb
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical


n_classes=5

e=emb()
arc=DenseArchs(n_classes)
face_model=arc.arch()

x_data=[]
y_data=[]

learning_rate=0.01
epochs=27
batch_size=32

people=os.listdir('people')

for x in people:
    for i in os.listdir('people/'+x):
        img=cv2.imread('people'+'/'+x+'/'+i,1)
        img=cv2.resize(img,(160,160))
        img=img.astype('float')/255.0
        img=np.expand_dims(img,axis=0)
        embs=e.calculate(img)
        x_data.append(embs)
        y_data.append(int(x[-1]))


x_data=np.array(x_data,dtype='float')
y_data=np.array(y_data)
y_data=y_data.reshape(len(y_data),1)
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.1,random_state=77)
y_train=to_categorical(y_train,num_classes=n_classes)
y_test=to_categorical(y_test,num_classes=n_classes)

o=Adam(lr=learning_rate,decay=learning_rate/epochs)
face_model.compile(optimizer=o,loss='categorical_crossentropy')
face_model.fit(x_train,y_train,batch_size=batch_size,epochs=epochs,shuffle='true',validation_data=(x_test,y_test))
face_model.save('face_reco2.MODEL')
print(x_data.shape,y_data.shape)
