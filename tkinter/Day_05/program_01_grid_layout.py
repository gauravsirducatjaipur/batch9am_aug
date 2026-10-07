import tkinter as tk

root = tk.Tk()
root.title("Grid Example")
root.geometry("500x300")

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root).grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root).grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Submit").grid(row=2, column=1, pady=20)

root.mainloop()
