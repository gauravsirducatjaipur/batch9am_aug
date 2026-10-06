import tkinter as tk

def on_button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Button Example")
root.geometry("400x200")


# Create a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)

# Run the application
root.mainloop()