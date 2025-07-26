from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry('400x400')
root.title('memory game')
root.config(bg='black')

pairs= ['$','$','&','&','*','*','#','#','!','!','~','~']
random.shuffle(pairs)
print(pairs)

first_btn=""
first_btn_value =""
count=0
r=False

def btnclicked(btn , pos):
    global first_btn, first_btn_value,count,r
    
    if btn["text"] == "":
        btn['text']= pairs[pos]
        if first_btn == "":
            first_btn = btn
            first_btn_value = pairs[pos]
        else:
            if first_btn_value==btn['text']:
                print('its a match')
                messagebox.showinfo('','good job')
                count+=1
                if count ==6 :
                    r = messagebox.askyesno('','do you wish to replay') 
                first_btn['state']=DISABLED
                btn['state']=DISABLED
                first_btn=''
                if r:
                    replay()
                else:
                    root.destroy()
            else:
                messagebox.showwarning('','try again')
                first_btn['text']=''
                btn["text"]=''
                first_btn = ''
                first_btn_value=''

def replay():
    global first_btn,first_btn_value,count,r
    random.shuffle(pairs)
    first_btn = ''
    first_btn_value=''
    count=0
    r=False
    for btn in button:
        btn["text"]=''
        btn["state"]=NORMAL


            

b0 = Button(root,text='',bg='darkgrey',fg='cyan',width=4,height =4, font=("Arial",14),command=lambda:btnclicked(b0,0))
b1 = Button(root,text='',bg='darkgrey',fg='cyan',width=4,height =4, font=("Arial",14),command=lambda:btnclicked(b1,1))
b2 = Button(root,text='',bg='darkgrey',fg='cyan',width=4, height =4, font=("Arial",14),command=lambda:btnclicked(b2,2))
b3 = Button(root,text='',bg='darkgrey',fg='cyan',width=4,height =4, font=("Arial",14),command=lambda:btnclicked(b3,3))
b4 = Button(root,text='',bg='darkgrey',fg='cyan',width=4,height =4, font=("Arial",14),command=lambda:btnclicked(b4,4))
b5 = Button(root,text='',bg='darkgrey',fg='cyan',width=4,height =4, font=("Arial",14),command=lambda:btnclicked(b5,5))
b6 = Button(root,text='',bg='darkgrey',fg='cyan',width=4,height =4, font=("Arial",14),command=lambda:btnclicked(b6,6))
b7 = Button(root,text='',bg='darkgrey',fg='cyan',width=4,height =4, font=("Arial",14),command=lambda:btnclicked(b7,7))
b8 = Button(root,text='',bg='darkgrey',fg='cyan',width=4,height =4, font=("Arial",14),command=lambda:btnclicked(b8,8))
b9 = Button(root,text='',bg='darkgrey',fg='cyan',width=4,height =4, font=("Arial",14),command=lambda:btnclicked(b9,9))
b10 = Button(root,text='',bg='darkgrey',fg='cyan',width=4,height =4, font=("Arial",14),command=lambda:btnclicked(b10,10))
b11= Button(root,text='',bg='darkgrey',fg='cyan',width=4,height =4, font=("Arial",14),command=lambda:btnclicked(b11,11))

replay_btn=Button(root,text='replay',bg='orange',command=lambda:replay())


b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)

b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)
replay_btn.grid(row=3,column=4)

button=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]

root.mainloop()