from tkinter import *
import sqlite3
import os 
from tkinter import messagebox
import cv2 as cv


class Student:
    def __init__(self):
        win = Tk()
        win.geometry('400x400')
        win.title('attendance system')
        win.config(bg='#222')
        


        Label(win,text='student Name: ',font=('Arial',12),bg='#222',fg='white').grid(row=0,column=0,pady=5)
        self.name = Entry(win)
        self.name.grid(row=0,column=1,pady=5)
        Label(win,text='student ID: ',font=('Arial',12),bg='#222',fg='white').grid(row=1,column=0,pady=5)
        self.id = Entry(win)
        self.id.grid(row=1,column=1,pady=5)
        Label(win,text='student Class: ',font=('Arial',12),bg='#222',fg='white').grid(row=2,column=0,pady=5)
        self.Sclass = Entry(win)
        self.Sclass.grid(row=2,column=1,pady=5)
        Button(win,text='submit',command=lambda:saveData(self)).grid(row=3,columnspan=2,pady=5)


        def saveData(self):
            conn = sqlite3.connect('attendencesytem.db')
            conn.execute("""
                        create table if not exists student (id integar, name text,class text)
                        """)
            
            print(self.name.get(),self.id.get(),self.Sclass.get())
            
            if self.name.get()=='':
                messagebox.showerror('sample data','enter the name')
            
            elif self.id.get()=='':
                messagebox.showerror('sample data','enter the ID')
            
            elif self.Sclass.get()=='':
                messagebox.showerror('sample data','enter the class')
            else:
                conn.execute("insert into student( id, name, class) values(:id, :name, :class)",
                             {
                                'name':self.name.get(),
                                'id':self.id.get(),
                                'class':self.Sclass.get()
                             })
                messagebox.showinfo('add student','saved data successfully')
                conn.commit()
                saveface(self)

        def saveface(self):
                path = 'attendencesystem/student-images/'+str(self.name.get()+'_'+str(self.id.get()))
                mode = 0o666
                os.mkdir(path,mode)
                cap = cv.VideoCapture(0)
                img_id = 0
                while True:
                     ret , my_frame = cap.read()
                     if my_frame is not None:
                          img_id+=1

                     face = cv.cvtColor(my_frame,cv.COLOR_BGR2GRAY)
                     finalpath =  path + '/' + str(self.name.get()) + '_' + str(img_id)+'.jpg'
                     cv.imwrite(finalpath, face)
                     cv.imshow(str(self.name.get()), face)
                     if cv.waitKey(1) == 13 or img_id == 100:
                          break
                     
                cap.release()
                cv.destroyAllWindows()
                     

        win.mainloop()