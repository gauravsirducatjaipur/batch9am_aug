from tkinter import *

def on_button_click():
    print("Button clicked!")

root = Tk()
root.title("Button Example")
root.geometry("500x300")

button = Button(root, text="Click Me", command=on_button_click)
button.pack(pady=30)

root.mainloop()
