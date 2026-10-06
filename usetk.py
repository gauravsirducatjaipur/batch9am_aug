import tkinter as tk

def Sum():
  print("Function has been called successfully")

root = tk.Tk();
root.title("Tkinter Example")
root.geometry("800x400")

label1 = tk.Label(root, text="Enter first number : ")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

button1 = tk.Button(root, text="Addition", command=Sum)
button1.pack()

root.mainloop();
