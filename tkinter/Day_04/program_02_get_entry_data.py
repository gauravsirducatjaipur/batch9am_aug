from tkinter import *

def show_data():
    data = entry.get()
    print(data)

root = Tk()
root.title("Entry Example")
root.geometry("500x300")

entry = Entry(root)
entry.pack(pady=20)

Button(root, text="Show Data", command=show_data).pack()

root.mainloop()
