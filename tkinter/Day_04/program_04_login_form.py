from tkinter import *

def login():
    username = username_entry.get()
    password = password_entry.get()
    print("Username:", username)
    print("Password:", password)

root = Tk()
root.title("Login Form")
root.geometry("500x300")

Label(root, text="Username").pack(pady=5)
username_entry = Entry(root)
username_entry.pack(pady=5)

Label(root, text="Password").pack(pady=5)
password_entry = Entry(root, show="*")
password_entry.pack(pady=5)

Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()
