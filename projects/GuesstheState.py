from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry('400x300')
root.title('guess the state ')
root.config(bg='cyan')

state_lst = ["Andhra Pradesh", "Assam", "Arunachal Pradesh", "Bihar", "Goa", 
         "Gujarat", "Jammu and Kashmir", "Jharkhand", "West Bengal", "Karnataka", "Kerala", 
         "Madhya Pradesh", "Maharashtra",
         "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Orissa", "Punjab",
         "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura", "Uttaranchal", 
         "Uttar Pradesh", "Haryana", "Himachal Pradesh", "Chhattisgarh"]

statelbl= Label(root,text='STATE',font=('arial',25),fg='black',bg='cyan')

statelbl.pack()

state=''

def jumblestate():
  global state
  state=random.choice(state_lst).upper()
  wordlist=list(state)
  random.shuffle(wordlist)
  shuffledword = ''
  for w in wordlist:
    shuffledword+=w
  statelbl['text']=shuffledword 
userans=StringVar()
score=0
def checkans():
  global score
  if state == userans.get().upper():
    score+=1
    scorelbl['text']='score: ' + str(score)
    response= messagebox.askyesno('aa','correct answer do you wish to go to the next level')
  else:
    response= messagebox.askyesno('aa','wrong answer '+state+' is the answer do you wish to go to the next level')
  if response:
    nextquest()
  else:
    root.destroy()

pos=0
def showhint():
  global state , pos
  hintlbl['text'] += state[pos]
  pos+=1
  if pos >= len(state):
    hintlbl['text']= 'the name of the state is \n' +  state
    pos=len(state) -1   
    ans['state']=DISABLED
    response = messagebox.askyesno('try again???','do you wat to continue???')
    if response:
      nextquest()
    else:
      root.destroy()

def nextquest():
  global pos
  jumblestate()
  userans.set('')
  ans['state']=NORMAL
  pos = 0
  hintlbl['text']=''



    
ans = Entry(root,text='',width=15,font=('popins',12),textvariable=userans) # type: ignore
hintbtn=Button(root,text='hint',width=10,bg='powderblue',fg='black',command=lambda:showhint())
submitbtn=Button(root,text='submit',width=10,bg='powderblue',fg='black',command=lambda:checkans())
hintlbl=Label(root,text='',font=('poppins',15),fg='black',bg='cyan')
scorelbl=Label(root,text='',font=('poppins',15),fg='black',bg='cyan')
submitbtn.pack()
ans.pack()
hintbtn.pack()
hintlbl.pack()
scorelbl.pack()
jumblestate()

root.mainloop()