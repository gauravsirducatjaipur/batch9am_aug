from tkinter import *

def show_data():
    data = entry.get()
    label.config(text="Hello " + data)

root = Tk()
root.title("Entry and Label")
root.geometry("500x300")

label = Label(root, text="Enter your name")
label.pack(pady=10)

entry = Entry(root)
entry.pack(pady=10)

Button(root, text="Submit", command=show_data).pack(pady=10)

root.mainloop()
