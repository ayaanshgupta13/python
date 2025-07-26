from tkinter import *
from addstudent import *
from showgallery import *
from traindata import *
from markattendence import *
from ShowRecords import *

root = Tk()
root.geometry('400x400')
root.title('attendance system')
root.config(bg='#333')

def getstudent():
    Student()

def showstudent():
    DisplayGallery()

def traindata():
    TrainFaces()

def markattendence():
    Mark()

def showrecords():
    ShowAttendance()


addimg = PhotoImage(file='attendencesystem/app-images/add-user.png')
addbtn = Button(root,image=addimg,bg='#333',command=lambda:getstudent()).grid(row=0,column=0,padx=15)
Label(root,text='Add student',bg='#333',fg='cyan').grid(row=1,column=0)


galimg = PhotoImage(file='attendencesystem/app-images/picture.png')
galbtn = Button(root,image=galimg,bg='#333',command=lambda:showstudent()).grid(row=0,column=1,padx=15)
Label(root,text='Show Students',bg='#333',fg='cyan').grid(row=1,column=1)

traindatai = PhotoImage(file='attendencesystem/app-images/book.png')
traindatab = Button(root,image=traindatai,bg='#333',command=lambda:traindata()).grid(row=0,column=2,padx=15)
Label(root,text='Train Data',bg='#333',fg='cyan').grid(row=1,column=2)

recordi = PhotoImage(file="attendencesystem/app-images/record.png")
recordl = Button(root,image=recordi,bg='#333',command=lambda:showrecords()).grid(row=0,column=3)
Label(root,text='Show Attendence',bg='#333',fg='cyan').grid(row=1,column=3)

facereci = PhotoImage(file='attendencesystem/app-images/face-recognition.png')
facerecl = Button(root,image=facereci,bg='#333',command=lambda:markattendence()).grid(row=2,columnspan=4)
Label(root,text='Mark attendence',bg='#333',fg='cyan',font=('Arial',15)).grid(row=3,columnspan=4)



root.mainloop()