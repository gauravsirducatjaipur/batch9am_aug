import tkinter as tk
from tkinter import Menu

def new_file():
    print("New")

def cut_text():
    print("Cut")

def about():
    print("About Application")

root = tk.Tk()
root.title("Menu Application")
root.geometry("600x400")

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.mainloop()
