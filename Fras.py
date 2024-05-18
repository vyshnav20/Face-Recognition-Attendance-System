import cv2
import numpy as np
import os
from tqdm import tqdm
import mtcnn
from PIL import Image
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import time

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import keras
from keras.models import Sequential,Model
from keras.layers import Dense,Activation,Input
from keras.utils import to_categorical
from keras.layers import Conv2D, MaxPool2D, Flatten

def cnn_model(input_shape,labels):
    model=Sequential()
    
    model.add(Conv2D(64,(3,3),padding="valid",activation="relu",input_shape=input_shape))
    model.add(Conv2D(64,(3,3),padding="valid",activation="relu",input_shape=input_shape))
    model.add(MaxPool2D(pool_size=(2,2)))
    model.add(Conv2D(128,(3,3),padding="valid",activation="relu"))
    model.add(Conv2D(128,(3,3),padding="valid",activation="relu"))
    model.add(MaxPool2D(pool_size=(2,2)))
    model.add(Flatten())
    model.add(Dense(128,activation="relu"))
    model.add(Dense(64,activation="relu"))
    model.add(Dense(len(labels)))
    model.add(Activation("softmax"))
    
    model.summary()
    model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
    
    return model


def Crete_Folder_Images(name, directory, tn):
    # Creating directory in the file
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print('DIRECTORY with name %s EXIST'%name)
    # Opening vedio mode with frontal face detector
    detector=mtcnn.MTCNN()
    cam=cv2.VideoCapture(0)
    size =(100, 100)
    for i in tqdm(range(1, 1+ tn)):
        ret,img=cam.read()
        faces=detector.detect_faces(img)
        for face in faces:
            bounding_box = face['box']
            x=bounding_box[0]
            y=bounding_box[1]
            w=bounding_box[2]
            h=bounding_box[3]
            x1,y1=abs(x),abs(y)
            x2,y2=x1+w,y1+h
            face=img[y1:y2,x1:x2]
            image=Image.fromarray(face)
            image=image.resize(size)
            face_array=np.asarray(image)
            cv2.imwrite('images/'+str(name)+'/'+str(name)+'_'+str(i)+'.jpg', face_array)  #for GRAY SCALE IMAGES

            # cv2.imwrite(directory+'/'+str(name)+'-'+str(sn)+'.jpg'
            #             ,img[y:y+h,x:x+w])  # FOR COLOR IMAGES
            cv2.putText(img,str(i),(25,25),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow('Sample Collector',img)
            cv2.waitKey(200)
            
    
    cam.release()
    cv2.destroyAllWindows()
    print('TASK COMPLETED')


def print_progress(val,val_len,folder,bar_size=20):
    prog="#"*round((val)*bar_size/val_len)+" "*round((val_len-(val))*bar_size/val_len)
    if val==0:
        print("",end="\n")
    else:
        print("[%s] (%d samples)\t label : %s \t\t" % (prog,val+1,folder), end="\r")
        
def register():
    import mysql.connector  
    name=input("Enter name:")
    i=float(input("Enter id:"))
    g=input("M or F")
    ph=int(input("Enter Phone Number"))
    ''''mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras')  
    mycursor = mydb.cursor()

    sql = "INSERT INTO student VALUES (%s,%s, %s,%s)"
    val = (name,i,ph,g)
    mycursor.execute(sql, val)

    mydb.commit()'''
    
    dir='images/'+name  
    #Crete_Folder_Images(name,dir,5)
    
    dir='download/'
    names=[]
    images=[]
    for folder in os.listdir(dir):
        files=os.listdir(os.path.join(dir,folder))
        for i,name in enumerate(files):
            img=cv2.imread(os.path.join(dir+folder,name))
            cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            images.append(img)
            names.append(folder)
            print_progress(i,len(files),folder)
    time.sleep(5)
    print("no:of samples :",len(names))
    le=LabelEncoder()
    le.fit(names)
    labels=le.classes_
    name_vec=le.transform(names)
    categorical_name_vec=to_categorical(name_vec)

    x_train,x_test,y_train,y_test=train_test_split(np.array(images,dtype=np.float32),np.array(categorical_name_vec),test_size=0.15,random_state=42)

    input_shape=x_train[0].shape
    EPOCHS=10
    BATCH_SIZE=32

    model=cnn_model(input_shape,labels)
    history=model.fit(x_train,y_train,epochs=EPOCHS,batch_size=BATCH_SIZE,shuffle=True,validation_split=0.15)