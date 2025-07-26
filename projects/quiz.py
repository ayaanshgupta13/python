from tkinter import *
from tkinter import messagebox
import random
from tkinter import ttk

root = Tk()
root.geometry('400x300')
root.title('quiz game')
root.config(bg='cyan')

notebook = ttk.Notebook(root)
tab2 = Frame(notebook,bg="lightgreen")
tab3 = Frame(notebook,bg="orange") 
notebook.add(tab2,text="guess the state")
notebook.add(tab3,text="guess the flag")

state_lst = ["Andhra Pradesh", "Assam", "Arunachal Pradesh", "Bihar", "Goa", 
         "Gujarat", "Jammu and Kashmir", "Jharkhand", "West Bengal", "Karnataka", "Kerala", 
         "Madhya Pradesh", "Maharashtra",
         "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Orissa", "Punjab",
         "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura", "Uttaranchal", 
         "Uttar Pradesh", "Haryana", "Himachal Pradesh", "Chhattisgarh"]

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

statelbl= Label(tab2,text='STATE',font=('arial',25),fg='black',bg='lightgreen')

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
    tab3.destroy()

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
      tab3.destroy()

def nextquest():
  global pos
  jumblestate()
  userans.set('')
  ans['state']=NORMAL
  pos = 0
  hintlbl['text']=''

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
      break
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
    
ans = Entry(tab2,text='',width=15,font=('popins',12),textvariable=userans) # type: ignore
hintbtn=Button(tab2,text='hint',width=10,bg='lightgreen',fg='black',command=lambda:showhint())
submitbtn=Button(tab2,text='submit',width=10,bg='lightgreen',fg='black',command=lambda:checkans())
hintlbl=Label(tab2,text='',font=('poppins',15),fg='black',bg='lightgreen')
scorelbl=Label(tab2,text='',font=('poppins',15),fg='black',bg='lightgreen')
submitbtn.pack()
ans.pack()
hintbtn.pack()
hintlbl.pack()
scorelbl.pack()

ans = StringVar()
hlbl = Label(tab3, text="Guess the Flag below",font=("Arial, 20"),fg="white",bg="orange")
lbl = Label(tab3, image=f1, bg="orange")
aEntry = Entry(tab3, textvariable=ans)
btn = Button(tab3, text="SUBMIT", bg="orange", fg="white", command=lambda:btnClick())
scorelbl=Label(tab3,text='',fg='white',font=('Arial,15'),bg='orange')
Labl=Label(tab3,text='')

hlbl.pack()
lbl.pack()
aEntry.pack()
btn.pack()
scorelbl.pack()
Labl.pack()

getRandomFlag()

notebook.pack(expand=True,fill="both")
jumblestate()

tab3.mainloop()