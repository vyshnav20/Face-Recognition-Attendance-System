import schedule
import time
import datetime
import mtcnn
import os
import cv2


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

job.c=0
job.p=0
schedule.every().day.at("10:17").do(job)
while True:
    # Run pending scheduled jobs
    schedule.run_pending()
    time.sleep(1)
