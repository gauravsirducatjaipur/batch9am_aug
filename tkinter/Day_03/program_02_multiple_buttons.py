from tkinter import *

def python_click():
    print("Python clicked")

def java_click():
    print("Java clicked")

def mern_click():
    print("MERN clicked")

root = Tk()
root.title("Course Buttons")
root.geometry("500x300")

Button(root, text="Python", command=python_click).pack(pady=10)
Button(root, text="Java", command=java_click).pack(pady=10)
Button(root, text="MERN", command=mern_click).pack(pady=10)

root.mainloop()
