import tkinter as tk

def about():
    window = tk.Toplevel(root)
    window.title("About")
    window.geometry("400x250")

    tk.Label(window, text="Student Management System",
             font=("Arial", 16)).pack(pady=30)

    tk.Button(window, text="Close",
              command=window.destroy).pack()

root = tk.Tk()
root.title("Main Window")
root.geometry("500x300")

tk.Button(root, text="About", command=about).pack(pady=50)

root.mainloop()
