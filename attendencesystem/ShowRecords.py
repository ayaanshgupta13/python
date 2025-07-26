from tkinter import *
from tkinter import ttk
import csv
import os
class ShowAttendance():
    def __init__(self, master=None):
        att = Toplevel(master) 
        att.title("Attendance Records")
        att.geometry('500x500')
        att.config(bg='#333')
        #create notbook widget
        notebook  = ttk.Notebook(att)
        # fpath = os.path('AttendanceSystemFri730/attendance')
        files = os.listdir('attendencesystem/attendence')
        print(files)
        # edit
        colorcode = "#404040"
        for file in files:
            print(file[:-4])
            tab = Frame(notebook, bg=colorcode)
            notebook.add(tab, text=file[:-4])
            c = int(colorcode[1:]) + 1000
            colorcode = "#" + str(c)
            filepath=os.path.join('attendencesystem/attendence',file)
            columns = ["StudentID","StudentName","Time"]
            tree=ttk.Treeview(tab,columns=columns,show="headings",style="Custom1.Treeview")
            tree.tag_configure('heading', background = "#FFE4C4",foreground="#8A2BE2")
            tree.tag_configure('odd', background = "#7FFFD4",foreground="#00008B")
            tree.tag_configure('even', background = "#008B8B",foreground="#7FFFD4")
            tree.pack(expand=True,fill='both')
            with open(filepath) as file:
                csvFile = csv.reader(file)
                i=0
                for lines in csvFile:
                    print(lines)
                    if i==0:
                        tree.insert("", "end", values=lines,tags="heading")
                    elif i%2 == 0:
                        tree.insert("", "end", values=lines,tags="even")
                    else:
                        tree.insert("", "end", values=lines,tags="odd")
                    i+=1                        
                    
                    #     y="grey"
            

        # edit
        
        notebook.pack(expand=True, fill="both")

        att.mainloop()