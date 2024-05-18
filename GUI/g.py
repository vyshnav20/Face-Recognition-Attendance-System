import mysql.connector  
import cv2
import numpy as np
import mtcnn
from PIL import Image
import os
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical

#register student
def data(name,i,ph,ge,pas,d):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s)"
    val = (name,i,ph,ge,d,pas)
    mycursor.execute(sql, val)

    mydb.commit()
    mycursor.close()
    mydb.close()


#student samples
def sample(name,dir,n):
        os.makedirs(dir)
        detector=mtcnn.MTCNN()
        cam=cv2.VideoCapture(0)
        size =(100, 100)
        for i in range(1,n+1):
            cv2.waitKey(200)
            ret,img=cam.read()
            pixels=np.asarray(img)
            faces=detector.detect_faces(img)
            for res in faces:
                bounding_box = res['box']
                x=bounding_box[0]
                y=bounding_box[1]
                w=bounding_box[2]
                h=bounding_box[3]
                x1,y1=abs(x),abs(y)
                x2,y2=x1+w,y1+h
                face=pixels[y1:y2,x1:x2]
                image=Image.fromarray(face)
                image=image.resize(size)
                face_array=np.asarray(image)
                
                cv2.imwrite(dir+'/'+str(name)+'_'+str(i)+'.jpg',face_array) 
                
                cv2.rectangle(img,(bounding_box[0], bounding_box[1]),(bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),(0,155,255),2)
                
                cv2.waitKey(200)
                cv2.putText(face_array,str(i),(25,25),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                cv2.imshow('DAtaset Creator',face_array)
            
        cv2.waitKey(500)
        cam.release()
        cv2.destroyAllWindows()

#student details        
def select():
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "select * from student"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return result

#password updation    
def pass_update(i,p):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "update student set password=%s where Roll_No=%s"
    val=(p,i)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()

def rollno(i):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "select name from student where Roll_no=%s"
    val=(i,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return(len(result))
    

#update phone number
def db_update(i,ph):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "update student set Phone_Number=%s where Roll_No=%s"
    val=(ph,i)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    
#delete student
def db_del(i):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "delete from student where Roll_No=%s"
    val=(i,)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()

#student login
def logins_db(id):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "select Password from student where Roll_no=%s"
    val=(id,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return result

#studnet details
def st_db(id):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "select Name,Roll_No,Phone_Number,Gender from student where Roll_no=%s"
    val=(id,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return result

#teacher login
def logint_db(id):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "select Password from teacher where Id=%s"
    val=(id,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    
    return result

#teacher details
def tr_db(id):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "select Name,Id,Phone_Number,Class_ID from teacher where Id=%s"
    val=(id,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return result

# class attendance        
def  db_atted():
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "SELECT s.Name as student_name,a.student_id,COUNT(*) as total_classes,SUM(CASE WHEN a.attendance_status = 'present' THEN 1 ELSE 0 END) as total_present,SUM(CASE WHEN a.attendance_status = 'absent' THEN 1 ELSE 0 END) as total_absent, TRUNCATE((SUM(CASE WHEN a.attendance_status = 'present' THEN 1 ELSE 0 END) / COUNT(*)) * 100,2) as attendance_percentage FROM attendance a JOIN student s ON s.Roll_No = a.student_id GROUP BY a.student_id"
    
    mycursor.execute(sql)
    result=mycursor.fetchall()    
    mycursor.close()
    mydb.close()
    return result
    
# subject-wise attendance
def  db_sub_atted():
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "select 'Total Hours' as student_name,'-',TRUNCATE(SUM(CASE WHEN a.Subject_id='cs01' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs01,TRUNCATE(SUM(CASE WHEN a.Subject_id='cs02' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs02, TRUNCATE(SUM(CASE WHEN a.Subject_id='cs03' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs03, TRUNCATE(SUM(CASE WHEN a.Subject_id='cs04' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs04, TRUNCATE(SUM(CASE WHEN a.Subject_id='cs05' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs05 FROM attendance a UNION SELECT s.Name as student_name, Student_Id, SUM(CASE WHEN a.Subject_id='cs01' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs01_p, SUM(CASE WHEN a.Subject_id='cs02' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs02_p,SUM(CASE WHEN a.Subject_id='cs03' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs03_p, SUM(CASE WHEN a.Subject_id='cs04' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs04_p, SUM(CASE WHEN a.Subject_id='cs05' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs05_p FROM attendance a JOIN student s on s.Roll_No=a.Student_Id GROUP BY a.Student_Id"
    
    mycursor.execute(sql)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return result

# attendance on a date
def db_date_atted(d):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "select 'Total Hours' as student_name,'-',TRUNCATE(SUM(CASE WHEN a.Subject_id='cs01' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs01,TRUNCATE(SUM(CASE WHEN a.Subject_id='cs02' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs02,TRUNCATE(SUM(CASE WHEN a.Subject_id='cs03' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs03,TRUNCATE(SUM(CASE WHEN a.Subject_id='cs04' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs04,TRUNCATE(SUM(CASE WHEN a.Subject_id='cs05' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs05 FROM attendance a WHERE date = %s UNION SELECT s.Name as student_name, Student_Id, SUM(CASE WHEN a.Subject_id='cs01' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs01_p, SUM(CASE WHEN a.Subject_id='cs02' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs02_p,SUM(CASE WHEN a.Subject_id='cs03' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs03_p,SUM(CASE WHEN a.Subject_id='cs04' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs04_p,SUM(CASE WHEN a.Subject_id='cs05' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs05_p FROM attendance a JOIN student s on s.Roll_No=a.Student_Id WHERE date = %s GROUP BY a.Student_Id"
    val=(d,d,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return result

#marks details
def db_marks(i,s):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "SELECT SUM(mark) as percentage FROM mark WHERE student_id = %s AND sem = %s GROUP BY subject_id UNION SELECT ROUND((SUM(mark) / (COUNT(subject_id))), 2) as percentage FROM mark WHERE student_id = %s AND sem = %s" 
    val=(i,s,i,s,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return result

#student attendance
def stud_db_attd(i):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "SELECT COUNT(*) as total_classes,SUM(CASE WHEN a.attendance_status = 'present' THEN 1 ELSE 0 END) as total_present,SUM(CASE WHEN a.attendance_status = 'absent' THEN 1 ELSE 0 END) as total_absent, TRUNCATE((SUM(CASE WHEN a.attendance_status = 'present' THEN 1 ELSE 0 END) / COUNT(*)) * 100,2) as attendance_percentage FROM attendance a where student_id=%s" 
    val=(i,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return result

#student- subject-wise attendance    
def st_sub_db_attd(i):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "select TRUNCATE(SUM(CASE WHEN a.Subject_id='cs01' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs01,TRUNCATE(SUM(CASE WHEN a.Subject_id='cs02' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs02, TRUNCATE(SUM(CASE WHEN a.Subject_id='cs03' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs03, TRUNCATE(SUM(CASE WHEN a.Subject_id='cs04' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs04, TRUNCATE(SUM(CASE WHEN a.Subject_id='cs05' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs05 FROM attendance a UNION SELECT SUM(CASE WHEN a.Subject_id='cs01' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs01_p, SUM(CASE WHEN a.Subject_id='cs02' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs02_p,SUM(CASE WHEN a.Subject_id='cs03' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs03_p, SUM(CASE WHEN a.Subject_id='cs04' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs04_p, SUM(CASE WHEN a.Subject_id='cs05' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs05_p FROM attendance a WHERE a.Student_Id=%s" 
    val=(i,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return result

#student- attendance on a date 
def st_db_date_atted(d,i):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "select TRUNCATE(SUM(CASE WHEN a.Subject_id='cs01' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs01,TRUNCATE(SUM(CASE WHEN a.Subject_id='cs02' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs02,TRUNCATE(SUM(CASE WHEN a.Subject_id='cs03' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs03,TRUNCATE(SUM(CASE WHEN a.Subject_id='cs04' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs04,TRUNCATE(SUM(CASE WHEN a.Subject_id='cs05' THEN 1 ELSE 0 END)/(COUNT(DISTINCT(a.Student_Id))),0) as cs05 FROM attendance a WHERE date = %s UNION SELECT SUM(CASE WHEN a.Subject_id='cs01' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs01_p, SUM(CASE WHEN a.Subject_id='cs02' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs02_p,SUM(CASE WHEN a.Subject_id='cs03' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs03_p,SUM(CASE WHEN a.Subject_id='cs04' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs04_p,SUM(CASE WHEN a.Subject_id='cs05' AND a.Attendance_status='present' THEN 1 ELSE 0 END) as cs05_p FROM attendance a  WHERE date = %s AND Student_Id=%s" 
    val=(d,d,i,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return result

# update attendance
def db_updt_attd(i,s,a,d):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "update attendance set Attendance_status=%s where student_id=%s and date=%s and subject_id=%s"
    val=(a,i,d,s,)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()

#subject details
def subjects():
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "select name from subject"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    mydb.close()
    return result

#student phone number
def phone(i):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "select phone_number from student where roll_no=%s"
    val=(i,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    mydb.close()
    return result

# update password
def updt_pass(i,p):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='fras_')  
    mycursor = mydb.cursor()

    sql = "update student set password=%s where roll_no=%s"
    val=(p,i,)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
