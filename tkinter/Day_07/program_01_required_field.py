from tkinter import *
from tkinter import messagebox

def submit():
    name = entry.get()
    if name == "":
        messagebox.showerror("Error", "Please enter name")
    else:
        messagebox.showinfo("Success", "Name submitted")

root = Tk()
root.title("Validation")
root.geometry("500x300")

Label(root, text="Name").pack(pady=10)
entry = Entry(root)
entry.pack(pady=10)
Button(root, text="Submit", command=submit).pack(pady=20)

root.mainloop()
