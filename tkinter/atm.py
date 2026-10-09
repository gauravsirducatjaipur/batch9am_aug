from tkinter import *
root=Tk()
root.title("ATM")
root.geometry("1200x700")
total_amount=30000

def Login():
    cardType=txtCardType.get().lower()
    cardNumber=txtCardNumber.get()
    name=txtName.get().lower()
    cvv=txtCVV.get()
    pin=txtPIN.get()

    if cardType in ["credit","debit"]:
        if cardNumber=="12345":
            if name=="sumit":
                if cvv=="123":
                    if pin=="8721":
                        lblDisplay.config(text="Login Successful\nWelcome to ATM",fg="green")
                    else:
                        lblDisplay.config(text="Invalid PIN number. Try again",fg="red")
                else:
                    lblDisplay.config(text="Invalid CVV",fg="red")
            else:
                lblDisplay.config(text="Invalid user",fg="red")
        else:
            lblDisplay.config(text="Invalid card number",fg="red")
    else:
        lblDisplay.config(text="Invalid card type",fg="red")



Label(root,text="Welcome to ATM",font=("Montserrat",25)).pack(pady=20)

Label(root,text="Enter Card Type (Debit/Credit)",font=("Montserrat",15)).pack(pady=10)

txtCardType=Entry(root,font=("Montserrat",15))
txtCardType.pack(pady=5)

Label(root,text="Enter Card Number",font=("Montserrat",15)).pack(pady=10)

txtCardNumber=Entry(root,font=("Montserrat",15))
txtCardNumber.pack(pady=5)

Label(root,text="Enter Name",font=("Montserrat",15)).pack(pady=10)

txtName=Entry(root,font=("Montserrat",15))
txtName.pack(pady=5)

Label(root,text="Enter CVV",font=("Montserrat",15)).pack(pady=10)

txtCVV=Entry(root,font=("Montserrat",15))
txtCVV.pack(pady=5)

Label(root,text="Enter PIN",font=("Montserrat",15)).pack(pady=10)

txtPIN=Entry(root,font=("Montserrat",15),show="*")
txtPIN.pack(pady=5)

Button(root,text="Login",font=("Montserrat",15),command=Login).pack(pady=20)

lblDisplay=Label(root,font=("Montserrat",15))
lblDisplay.pack(pady=10)

root.mainloop()