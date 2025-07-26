import os 
from tkinter import *
import numpy as np
from PIL import Image
import cv2
import cv2.face
from tkinter import messagebox

class TrainFaces():
    def __init__(self, master=None):
        win = Toplevel(master)
        win.title("Train Student Images")
        win.geometry("300x300")
        win.config(bg="#333")
        Button(win, text="TRAIN STUDENTS DATA", bg="#333", fg="cyan", command=lambda:self.trainSampleFaces()).pack()


    def trainSampleFaces(self):
        path = 'attendencesystem/student-images'
        print(path)

        directories = os.listdir(path)
        print(directories)
        faces = []

        
        names = []
        for d in directories:
            dirPath = os.path.join(path,d)
            if os.path.isdir(dirPath):
                print(d,">>>>>>>")
                id = d.split('_')   #fix
                print(id)       #fix
                names.append(int(id[1]))
                for image in os.listdir(dirPath):
                    print(image)
                    file_path = os.path.join(dirPath, image)
                    img = Image.open(file_path).convert('L')
                    imageNP = np.array(img, 'uint8')
                    # print(imageNP)
                    faces.append(imageNP)
                    cv2.imshow("Training", imageNP)
                    break
                    cv2.waitKey(1) == 13
        names = np.array(names)
        print(len(names), len(faces))
        #Train
        clf = cv2.face.LBPHFaceRecognizer_create()

        clf.train(faces, names)
        clf.write("attendencesystem/classifier.xml")  
        messagebox.showinfo('Training','Completed')
        cv2.destroyAllWindows()