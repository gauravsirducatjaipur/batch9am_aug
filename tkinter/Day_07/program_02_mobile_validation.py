from tkinter import *
from tkinter import messagebox

def submit():
    mobile = entry.get()

    if mobile == "":
        messagebox.showerror("Error", "Mobile is required")
    elif not mobile.isdigit():
        messagebox.showerror("Error", "Mobile must contain digits only")
    elif len(mobile) != 10:
        messagebox.showerror("Error", "Mobile must be 10 digits")
    else:
        messagebox.showinfo("Success", "Valid mobile number")

root = Tk()
root.title("Mobile Validation")
root.geometry("500x300")

Label(root, text="Mobile").pack(pady=10)
entry = Entry(root)
entry.pack(pady=10)
Button(root, text="Submit", command=submit).pack(pady=20)

root.mainloop()
