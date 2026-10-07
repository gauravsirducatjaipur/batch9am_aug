import tkinter as tk

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

root = tk.Tk()
root.title("Focus Example")
root.geometry("500x300")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

entry1.pack(pady=10)
entry2.pack(pady=10)
entry3.pack(pady=10)

entry1.bind("<Return>", focus_next_widget)
entry2.bind("<Return>", focus_next_widget)
entry3.bind("<Return>", focus_next_widget)

entry1.focus_set()

root.mainloop()
