from modelArch import DenseArchs
import cv2
import numpy as np
import os
from embedding import emb
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
e=emb()
arc=DenseArchs(3)
face_model=arc.arch()

x_data=[]
y_data=[]

learning_rate=0.01
epochs=27
batch_size=32
path1='satinder'
path2='saugat'
path3='mandeep'

files=os.listdir(path1)
for i in files:
    img=cv2.imread(path1+'/'+i,1)
    img=cv2.resize(img,(160,160))
    img=img.astype('float')/255.0
    img=np.expand_dims(img,axis=0)
    embs=e.calculate(img)
    x_data.append(embs)
    y_data.append(0)

files=os.listdir(path2)
for i in files:
    img=cv2.imread(path2+'/'+i,1)
    img=cv2.resize(img,(160,160))
    img=img.astype('float')/255.0
    img=np.expand_dims(img,axis=0)
    embs=e.calculate(img)
    x_data.append(embs)
    y_data.append(1)

files=os.listdir(path3)
for i in files:
    img=cv2.imread(path3+'/'+i,1)
    img=cv2.resize(img,(160,160))
    img=img.astype('float')/255.0
    img=np.expand_dims(img,axis=0)
    embs=e.calculate(img)
    x_data.append(embs)
    y_data.append(2)


x_data=np.array(x_data,dtype='float')
y_data=np.array(y_data)
y_data=y_data.reshape(len(y_data),1)
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.1,random_state=77)
y_train=to_categorical(y_train,num_classes=3)
y_test=to_categorical(y_test,num_classes=3)

o=Adam(lr=learning_rate,decay=learning_rate/epochs)
face_model.compile(optimizer=o,loss='categorical_crossentropy')
face_model.fit(x_train,y_train,batch_size=batch_size,epochs=epochs,shuffle='true',validation_data=(x_test,y_test))
face_model.save('face_reco.MODEL')
print(x_data.shape,y_data.shape)
