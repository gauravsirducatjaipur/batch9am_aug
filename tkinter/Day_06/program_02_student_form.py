from tkinter import *

def register():
    print("Name:", name.get())
    print("Email:", email.get())
    print("Mobile:", mobile.get())

root = Tk()
root.title("Student Registration")
root.geometry("600x400")

name = StringVar()
email = StringVar()
mobile = StringVar()

Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
Entry(root, textvariable=name).grid(row=0, column=1)

Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10)
Entry(root, textvariable=email).grid(row=1, column=1)

Label(root, text="Mobile").grid(row=2, column=0, padx=10, pady=10)
Entry(root, textvariable=mobile).grid(row=2, column=1)

Button(root, text="Register", command=register).grid(row=3, column=1, pady=20)

root.mainloop()
