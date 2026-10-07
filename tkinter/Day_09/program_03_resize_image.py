from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Resize Image")
root.geometry("800x500")

image = Image.open("photo.jpg")
image = image.resize((300, 200))

photo = ImageTk.PhotoImage(image)
Label(root, image=photo).pack(pady=30)

root.mainloop()
