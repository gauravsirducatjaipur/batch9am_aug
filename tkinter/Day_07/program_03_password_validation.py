from tkinter import *
from tkinter import messagebox

def submit():
    password = entry.get()

    if len(password) < 6:
        messagebox.showerror("Error", "Password must contain at least 6 characters")
    else:
        messagebox.showinfo("Success", "Valid Password")

root = Tk()
root.title("Password Validation")
root.geometry("500x300")

Label(root, text="Password").pack(pady=10)
entry = Entry(root, show="*")
entry.pack(pady=10)
Button(root, text="Submit", command=submit).pack(pady=20)

root.mainloop()
