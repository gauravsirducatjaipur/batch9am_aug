from tkinter import *

root = Tk()
root.title("Multiple Labels")
root.geometry("600x300")

Label(root, text="Name: Gaurav").pack(pady=10)
Label(root, text="Course: Python").pack(pady=10)
Label(root, text="Institute: Ducat").pack(pady=10)

root.mainloop()
