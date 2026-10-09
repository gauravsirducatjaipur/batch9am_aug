from tkinter import *

def python_click():
    print("Python clicked")
    lblDisplay.config(text="Python clicked")

def java_click():
    print("Java clicked")
    lblDisplay.config(text="Java clicked")

def mern_click():
    print("MERN clicked")
    lblDisplay.config(text="MERN clicked")

root = Tk()
root.title("Course Buttons")
root.geometry("500x300")


lblDisplay = Label(root, text="")
lblDisplay.pack(pady=10)

Button(root, text="Python", command=python_click).pack(pady=10)
Button(root, text="Java", command=java_click).pack(pady=10)
Button(root, text="MERN", command=mern_click).pack(pady=10)

root.mainloop()
