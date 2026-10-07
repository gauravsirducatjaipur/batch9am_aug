import tkinter as tk

def show_data(event):
    print("Enter key pressed")

root = tk.Tk()
root.title("Keyboard Event")
root.geometry("500x300")

entry = tk.Entry(root)
entry.pack(pady=30)
entry.bind("<Return>", show_data)

root.mainloop()
