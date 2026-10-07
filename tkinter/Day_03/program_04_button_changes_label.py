from tkinter import *

def change_text():
    label.config(text="Button Clicked!")

root = Tk()
root.title("Button and Label")
root.geometry("500x300")

label = Label(root, text="Click the button", font=("Arial", 18))
label.pack(pady=30)

Button(root, text="Click Me", command=change_text).pack()

root.mainloop()
