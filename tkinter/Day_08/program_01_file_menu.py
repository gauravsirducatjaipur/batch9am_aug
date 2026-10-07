import tkinter as tk
from tkinter import Menu

def new_file():
    print("New File")

def open_file():
    print("Open File")

def save_file():
    print("Save File")

root = tk.Tk()
root.title("Menu Example")
root.geometry("500x300")

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
