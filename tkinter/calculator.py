from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("1200x700")


def Addition():
  num1 = int(txtNum1.get())
  num2 = int(txtNum2.get())

  lblDisplay.config(text=f"Total is {num1 + num2}")

def Subtraction():
  pass

def Multiplication():
  pass

def Division():
  pass


Label(root, text="Welcome to Calculator", font=("Montserrat", 20)).pack(pady=20)

Label(root, text="Enter first number").pack(pady=10)

txtNum1 = Entry(root, font=("Montserrat", 15))
txtNum1.pack(pady=10)


Label(root, text="Enter second number").pack(pady=10)

txtNum2 = Entry(root, font=("Montserrat", 15))
txtNum2.pack(pady=10)


lblDisplay = Label(root, font=("Montserrat", 15))
lblDisplay.pack(pady=10)

Button(root, text="Addition", font=("Montserrat", 15), command=Addition).pack(pady=10)
Button(root, text="Subratction", font=("Montserrat", 15), command=Subtraction).pack(pady=10)
Button(root, text="Multiplication", font=("Montserrat", 15), command=Multiplication).pack(pady=10)
Button(root, text="Division", font=("Montserrat", 15), command=Division).pack(pady=10)

root.mainloop()
