from tkinter import *

root = Tk()
root.title("Label Alignment")
root.geometry("600x300")

Label(root, text="Left Side", anchor="w").pack(fill="x", padx=20, pady=10)
Label(root, text="Center", anchor="center").pack(fill="x", padx=20, pady=10)
Label(root, text="Right Side", anchor="e").pack(fill="x", padx=20, pady=10)

root.mainloop()
