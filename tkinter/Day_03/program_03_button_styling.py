from tkinter import *

def on_button_click():
    print("You clicked on me and I am a button...")

root = Tk()
root.title("Button Styling")
root.geometry("600x300")
root.configure(bg="lightblue")

button = Button(root, text="Click Me", command=on_button_click,
                bg="blue", fg="white", font=("Arial", 16),
                width=15, height=2)
button.pack(pady=50)

root.mainloop()
