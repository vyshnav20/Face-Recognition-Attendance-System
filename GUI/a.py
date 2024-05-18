import schedule
import time
import datetime
import mtcnn
import os
import cv2
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import mysql.connector  
from w import wh_msg,wh_p_msg

def attd(i,s,d,l):
    absent=[]
    for j in l:
        if j not in i:
            a="absent"
            absent.append(j)
        else:
            a="present"
        mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
        mycursor = mydb.cursor()
        sql = "INSERT INTO attendance VALUES (%s,%s, %s,%s)"
        val = (j,s,d,a,)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()
    ph=[]
    phn=[]
    current_date = datetime.date.today()
    d=str(current_date)
    ph=msg(absent)
    st=" is marked absent for class "+s+" on "+d
    wh_msg(ph,absent,st)    
    phn=percent_msg()
    st1="Attendance Percentage has dropped below 75%"
    wh_p_msg(phn,st1)

def percent_msg():
    p=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()
    sql = "SELECT student.phone_number FROM student INNER JOIN ( SELECT attendance.student_id, SUM(CASE WHEN attendance.attendance_status = 'Present' THEN 1 ELSE 0 END) / COUNT(*) AS attendance_percentage  FROM `attendance` GROUP BY attendance.student_id  HAVING `attendance_percentage` < 0.75 ) AS subquery ON student.`Roll_No` = subquery.student_id"
    mycursor.execute(sql,)
    result=mycursor.fetchall()
    for i in result[0]:
        p.append(str(i))            
    return p        

def msg(a):
    p=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()
    for j in a:
        sql = "select Phone_Number from student where Roll_no=%s"
        val=(j,)
        mycursor.execute(sql,val)
        result=mycursor.fetchall()
        for i in result[0]:            
            p.append(str(i))            
    return p

def face_recognition(n,labels,p):
    s=['cs01','cs02','cs03','cs04','cs05']    
    s1=[]
    detector=mtcnn.MTCNN()
    dir="E:/MIC/project/Code/New folder/GUI/Cls_Visuals/"
    file_list=[dir+f for f in os.listdir(dir)]
    c=0
    for i in file_list:        
        st=[]
        f=os.path.splitext(os.path.basename(file_list[c]))
        fn=str(f[0]).split('_')
        
        if(fn[1]==p):
            c+=1
            img=cv2.imread(i)
            cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=detector.detect_faces(img)

            for face in faces:            
                x, y, w, h = face['box']
                face_cropped = img[y:y+h, x:x+w]
                face_img=cv2.resize(face_cropped,(100,100))
                face_img=face_img.reshape(1,100,100,3)
                result=n.predict(face_img,verbose=0)
                idx=result.argmax(axis=1)
                label_text=labels[idx]
                st.append(str(label_text[0]))            
            
            for i in st:
                if i not in s1:
                    s1.append(i)
    attd(s1,s[int(p)-1],fn[0],labels)
        


def job():
    dir='Cls_Visuals/'
    current_date = datetime.date.today()
    d=str(current_date)
    job.c+=1
    job.p+=1
    cam=cv2.VideoCapture(0)
    size =(951, 551)
    ret,img=cam.read()
    img=cv2.resize(img,size) 
    current_date = datetime.date.today()
    d=str(current_date)   
    cv2.imwrite(dir+d+'_'+str(job.c)+'_'+str(job.p)+'.jpg',img)
    cv2.waitKey(200)
    cam.release()
    cv2.destroyAllWindows()
    if job.p==2:
        job.p=0


dir='E:/MIC/project/Code/New folder/download/'
images=[]
names=[]
for folder in os.listdir(dir):
    files=os.listdir(os.path.join(dir,folder))
    for i,name in enumerate(files):
        img=cv2.imread(os.path.join(dir+folder,name))
        cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    images.append(img)
    names.append(folder)
        

le=LabelEncoder()
le.fit(names)
labels=le.classes_
name_vec=le.transform(names)

n=load_model('E:/MIC/project/Code/New folder/fras.h5')
face_recognition(n,labels,'1')

'''

job.c=0
job.p=0
schedule.every().day.at("10:14").do(job)
schedule.every().day.at("9:40").do(job)
face_recognition(n,labels,'1')
schedule.every().day.at("10:40").do(job)
schedule.every().day.at("11:15").do(job)
face_recognition(n,labels,'2')
schedule.every().day.at("11:40").do(job)
schedule.every().day.at("12:15").do(job)
face_recognition(n,labels,'3')
schedule.every().day.at("13:40").do(job)
schedule.every().day.at("14:15").do(job)
face_recognition(n,labels,'4')
schedule.every().day.at("14:40").do(job)
schedule.every().day.at("15:15").do(job)
face_recognition(n,labels,'5')

while True:
    # Run pending scheduled jobs
    schedule.run_pending()
    time.sleep(1)




'''