from tkinter import *

root = Tk()
root.title("Image Example")
root.geometry("600x400")

photo = PhotoImage(file="logo.png")

Label(root, image=photo).pack(pady=30)

root.mainloop()
