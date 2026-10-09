from tkinter import *

root = Tk()
root.title("Label Styling")
root.geometry("600x300")
root.configure(bg="lightblue")

label = Label(root, text="Welcome to Python", bg="lightblue", fg="black", font=("Arial", 20))
label.pack(pady=30)

root.mainloop()
