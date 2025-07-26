from tkinter import*
import random
from tkinter import messagebox

root = Tk()
root.geometry('400x400')
root.title('memory game')
root.config(bg='#3a3b3c')




f1=PhotoImage(file='images/flags/brazil.png')
f2=PhotoImage(file='images/flags/france.png')
f3=PhotoImage(file='images/flags/germany.png')
f4=PhotoImage(file='images/flags/india.png')
f5=PhotoImage(file='images/flags/portugal.png')
f6=PhotoImage(file='images/flags/russia.png')
f7=PhotoImage(file='images/flags/south-korea.png')
f8=PhotoImage(file='images/flags/united-arab-emirates.png')
f9=PhotoImage(file='images/flags/united-states.png')

flags=[f1,f2,f3,f4,f5,f6,f7,f8,f9]

flags_dict={
    f1:'brazil',
    f2:'france',
    f3:'germany',
    f4:'india',
    f5:'portugal',
    f6:'russia',
    f7:'south-korea',
    f8:'united-arab-emirates',
    f9:['united-states','US','USA','United states of america'],

}

rf = ""
nf=0
cf=0
bl=''

def getRandomFlag():
  global rf,nf
  rf = random.choice(flags)
  lbl.config(image=rf)
  nf+=1

def btnClick():
  global rf,nf,cf,bl
  v=flags_dict.get(rf)
  if type(v)==list:
    for ele in v:
      if v.lower() == ans.get().lower():
        messagebox.showinfo('correct answer','you guessed it right')
        cf+=1
        break
      else:
        messagebox.showinfo('wrong answer','you guessed it wrong it is ' + ele)
  else:
    if v.lower() == ans.get().lower():
      messagebox.showinfo('correct answer','you guessed it right')
      cf+=1
  if ans.get() == bl:
    Labl['text']='please enter text'
  else:
    messagebox.showinfo('wrong answer','you guessed it wrong it is ' + v)
    btnClick()
          
  scorelbl['text']='score: '+ str(cf) + ' / '+str(nf)
  getRandomFlag()
  ans.set('')
  flags.remove(rf)
  



ans = StringVar()
hlbl = Label(root, text="Guess the Flag below",font=("Arial, 20"),fg="white",bg="#3a3b3c")
lbl = Label(root, image=f1, bg="#3a3b3c")
aEntry = Entry(root, textvariable=ans)
btn = Button(root, text="SUBMIT", bg="black", fg="white", command=lambda:btnClick())
scorelbl=Label(root,text='',fg='white',font=('Arial,15'),bg='#3a3b3c')
Labl=Label(root,text='')

hlbl.pack()
lbl.pack()
aEntry.pack()
btn.pack()
scorelbl.pack()
Labl.pack()

getRandomFlag()
root.mainloop()
