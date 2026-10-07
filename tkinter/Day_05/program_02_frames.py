import tkinter as tk

root = tk.Tk()
root.title("Frame Example")
root.geometry("600x400")

header = tk.Frame(root, bg="blue", height=80)
header.pack(fill="x")

body = tk.Frame(root, bg="lightgray")
body.pack(fill="both", expand=True)

footer = tk.Frame(root, bg="black", height=50)
footer.pack(fill="x")

tk.Label(header, text="Student Management System",
         bg="blue", fg="white", font=("Arial", 20)).pack(pady=20)

tk.Label(body, text="Student Details",
         font=("Arial", 18)).pack(pady=50)

tk.Label(footer, text="Copyright 2026",
         bg="black", fg="white").pack(pady=15)

root.mainloop()
