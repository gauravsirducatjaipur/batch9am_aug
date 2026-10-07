import tkinter as tk

def open_window():
    window = tk.Toplevel(root)
    window.title("Second Window")
    window.geometry("400x300")

    tk.Label(window, text="This is second window").pack(pady=50)

root = tk.Tk()
root.title("Toplevel Example")
root.geometry("500x300")

tk.Button(root, text="Open Window", command=open_window).pack(pady=50)

root.mainloop()
