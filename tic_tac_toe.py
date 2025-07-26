from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("TicTacToe✅")

turn = "X"
valueList = ["#","#","#","#","#","#","#","#","#"]
count = 0
def btnClick(b,pos):
  global turn, count
  if b["text"] == "":
    if turn == "X":
      b["text"] = "X"
      valueList[pos] = "X"
      turn = "O"
    else:
      b["text"] = "O"
      valueList[pos] = "O"
      turn = "X"
    count+=1
  print(valueList)
  print(count)
  checkWinner()

combinations = []
no_of_matches = 0
no_of_matches_x = 0
no_of_matches_o = 0 
winner = ""
def checkWinner():
  global combinations, winner, no_of_matches, no_of_matches_x, no_of_matches_o
  combinations.clear()
  combinations.append(valueList[0]+valueList[1]+valueList[2])
  combinations.append(valueList[0]+valueList[3]+valueList[6])
  combinations.append(valueList[0]+valueList[4]+valueList[8])
  combinations.append(valueList[1]+valueList[4]+valueList[7])
  combinations.append(valueList[2]+valueList[4]+valueList[6])
  combinations.append(valueList[2]+valueList[5]+valueList[8])
  combinations.append(valueList[3]+valueList[4]+valueList[5])
  combinations.append(valueList[6]+valueList[7]+valueList[8])

  if "XXX" in combinations:
    lbl["text"] = "X wins!!!"
    winner = "X"
    no_of_matches_x+=1
    no_of_matches+=1
    disableenable(False)
  elif "OOO" in combinations:
    lbl["text"] = "O wins!!!"
    winner ="O"
    no_of_matches_o+=1
    no_of_matches+=1
    disableenable(False)
  elif count == 9:
    lbl["text"] = "Draw!!!"
    winner ="Draw"
    no_of_matches+=1
    disableenable(False)


def disableenable(enabled):
  global buttons
  if enabled:
    for btn in buttons:
      btn["state"] = NORMAL
      btn["text"] = ""
  else:
    for btn in buttons:
      btn["state"] = DISABLED
      no_of_matches_lbl["text"] = "No of matches :" + str(no_of_matches)
      no_of_x_won_lbl["text"] = "No of matches X :" + str(no_of_matches_x)
      no_of_o_won_lbl["text"] = "No of matches O : "+ str(no_of_matches_o)


def replay():
  global count, valueList, combinations
  disableenable(True)
  lbl["text"] = " "
  valueList = ["#","#","#","#","#","#","#","#","#"]
  combinations = []
  count = 0

  
b1 = Button(root, text="", width=5,height=3,bg="Crimson", fg="white", font=("Poppins",12), command=lambda:btnClick(b1,0))
b2 = Button(root, text="", width=5,height=3,bg="Black", fg="white", font=("Poppins",12), command=lambda:btnClick(b2,1))
b3 = Button(root, text="", width=5,height=3,bg="Crimson", fg="white", font=("Poppins",12), command=lambda:btnClick(b3,2))

b4 = Button(root, text="", width=5,height=3,bg="Black", fg="white", font=("Poppins",12), command=lambda:btnClick(b4,3))
b5 = Button(root, text="", width=5,height=3,bg="Crimson", fg="white", font=("Poppins",12), command=lambda:btnClick(b5,4))
b6 = Button(root, text="", width=5,height=3,bg="Black", fg="white", font=("Poppins",12), command=lambda:btnClick(b6,5))

b7 = Button(root, text="", width=5,height=3,bg="Crimson", fg="white", font=("Poppins",12), command=lambda:btnClick(b7,6))
b8 = Button(root, text="", width=5,height=3,bg="Black", fg="white", font=("Poppins",12), command=lambda:btnClick(b8,7))
b9 = Button(root, text="", width=5,height=3,bg="Crimson", fg="white", font=("Poppins",12), command=lambda:btnClick(b9,8))

lbl = Label(root, text="", font=("Poppins",15), fg="green")

replayBtn = Button(root,text="Replay", bg="black", fg="Crimson", font=("Poppins",12), command=lambda:replay())

no_of_matches_lbl =  Label(root, text="", font=("Poppins",15), fg="blue")
no_of_x_won_lbl =  Label(root, text="", font=("Poppins",15), fg="blue")
no_of_o_won_lbl =  Label(root, text="", font=("Poppins",15), fg="blue")


b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)


b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)


b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

lbl.grid(row=3, columnspan=3)
replayBtn.grid(row=4, columnspan=3)
no_of_matches_lbl.grid(row=5, columnspan=3)
no_of_x_won_lbl.grid(row=6, columnspan=3)
no_of_o_won_lbl.grid(row=7, columnspan=3)


buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

root.mainloop()