from tkinter import *

def show_data():
    print(name.get())

root = Tk()
root.title("StringVar Example")
root.geometry("500x300")

name = StringVar()

Entry(root, textvariable=name).pack(pady=20)
Button(root, text="Show", command=show_data).pack()

root.mainloop()
