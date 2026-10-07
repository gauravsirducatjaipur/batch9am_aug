from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("JPEG Image")
root.geometry("800x500")

image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)

Label(root, image=photo).pack(pady=30)

root.mainloop()
