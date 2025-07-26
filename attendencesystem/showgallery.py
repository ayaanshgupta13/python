from tkinter import *
import os
from PIL import Image, ImageTk

class DisplayGallery():
    def __init__(self, master=None):
        gal = Toplevel(master)  # Create a new window as a child of the main window
        gal.title("Gallery")
        gal.geometry('600x600')
        gal.config(bg="#333")

        path = "attendencesystem\student-images"
        folders = os.listdir(path)

        r = 0
        col = 0

        self.photos = []  # List to store image references

        for folder in folders:
            folderpath = os.path.join(path, folder)
            files = os.listdir(folderpath)
            for f in files:
                filepath = os.path.join(folderpath, f)
                
                try:
                    img = Image.open(filepath)
                    img = img.resize((100, 100))  # Resize the image as needed
                    photo = ImageTk.PhotoImage(img)
                    self.photos.append(photo)  # Store reference to avoid garbage collection

                    pic = Label(gal, image=photo)
                    pic.grid(row=r, column=col, padx=10)

                    Label(gal, text=folder, bg="#333", fg="white", font=("poppins", 12)).grid(row=r + 1, column=col, padx=10)
                    col += 1

                    if col > 2:
                        col = 0
                        r += 2  # Increase by 2 to account for the image and the label
                    break    
                except Exception as e:
                    print(f"Error loading image {filepath}: {e}")
                
        gal.mainloop()
