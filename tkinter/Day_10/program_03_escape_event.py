import tkinter as tk

root = tk.Tk()
root.title("Escape Event")
root.geometry("500x300")

root.bind("<Escape>", lambda event: root.destroy())

tk.Label(root, text="Press ESC to exit",
         font=("Arial", 20)).pack(pady=100)

root.mainloop()
