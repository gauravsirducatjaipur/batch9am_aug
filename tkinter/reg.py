from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login Form")
root.geometry("600x400")



def login():
  uname = username.get()
  pwd = password.get()
  otp1 = otp.get()

  if uname =="":
    messagebox.showerror("Error", "Please enter username")
  elif pwd == "":
    messagebox.showerror("Error", "Please enter password")
  elif otp1 == "":
    messagebox.showerror("Error", "Please enter OTP")
  else:
    print("Username:", uname)
    print("Password:", pwd)
    print("OTP:", otp1)


username = StringVar()
password = StringVar()
otp = StringVar()

Label(root, text="Enter Username").grid(row=0, column=0, padx=10, pady=10)
Entry(root, textvariable=username).grid(row=0, column=1, padx=10, pady=10)


Label(root, text="Enter Password").grid(row=1, column=0, padx=10, pady=10)
Entry(root, textvariable=password).grid(row=1, column=1, padx=10, pady=10)


Label(root, text="Enter OTP").grid(row=2, column=0, padx=10, pady=10)
Entry(root, textvariable=otp).grid(row=2, column=1, padx=10, pady=10)

Button(root, text="Login", command=login).grid(row=3, column=1, pady=20)

root.mainloop()