import tkinter as tk

root = tk.Tk()
root.title("Registration Form")
root.geometry("600x400")

form = tk.Frame(root)
form.pack(pady=30)

tk.Label(form, text="Name").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(form).grid(row=0, column=1, padx=10, pady=10)

tk.Label(form, text="Email").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(form).grid(row=1, column=1, padx=10, pady=10)

tk.Label(form, text="Mobile").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(form).grid(row=2, column=1, padx=10, pady=10)

tk.Button(form, text="Register").grid(row=3, column=1, pady=20)

root.mainloop()
