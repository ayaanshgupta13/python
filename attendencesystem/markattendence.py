from tkinter import *
from tkinter import messagebox
import cv2
import sqlite3
from datetime import date,datetime
import csv

class Mark():
    found= True
    def __init__(self, master=None):
        def captureF():
            video_cap = cv2.VideoCapture(0)
            face_C=cv2.CascadeClassifier('attendencesystem/haarcascade_frontalface_default.xml')
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read('attendencesystem/classifier.xml')
            while True:
                ret, img= video_cap.read()

                img = recognise(img,clf,face_C)
                if img is None or img.shape[0] == 0 or img.shape[1] == 0:
                    messagebox.showerror("Error","image not found")
                else:
                    cv2.imshow("Face captured",img)
                
                    if cv2.waitKey(1) == 13:
                        break

            video_cap.release()
            cv2.destroyAllWindows()

        def save_attendance(stu_name,id):
            today = date.today()
            now = datetime.now()
            now2=now.strftime("%M:%S")
            print("date>>>>>>>>",today,now)
            print(stu_name)
            filen = f"attendencesystem/attendence/{today}.csv"
            print(filen)
            try:
                with open(filen,"r+",newline="") as csvfile:
                    datalist = csvfile.readlines()
                    print(datalist)
                    for line in datalist:
                        if id not in line:
                            datalist.append([id,stu_name,now2])
                            csv_writer = csv.writer(csvfile)
                            csv_writer.writerows(datalist)

            except:
                with open(filen,"w",newline="") as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(['stu_id',"stu_name","time"])
                    csv_writer.writerow([id,stu_name,now2])



        def recognise(img,clf,face_C):
                font = cv2.FONT_HERSHEY_SIMPLEX 
                conn = sqlite3.connect('attendencesytem.db')
                c= conn.cursor()
                if img is None:
                    print("image not found")
                else:
                    grey_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_C.detectMultiScale(img,1.2,5)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,0,255),3)
                        
                        id,predict = clf.predict(grey_image[y:y+h,x:x+y])
                        confidence = int((1-predict/300)*100)
                        c.execute(f"select name from student where id = {id}")
                        result = c.fetchone()
                        print(result)
                        if result:
                            stu_name = result[0]
                        if confidence>70:
                            cv2.putText(img,f'name: {stu_name}', (x,y - 20),font, 1.0,  (0, 0, 255),  2)
                            if self.found: 
                                save_attendance(stu_name , id)
                                self.found = False
                    return img
        captureF()
        
