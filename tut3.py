from tkinter import *

# Function to be called when the button is clicked
def on_button_click():
    print("Button clicked!")
    data = entry.get()
    data = "hello " + data
    label.config(text = data)

# Create the main window
root = Tk()
root.title("Tkinter Example")
root.geometry("800x300")
root.minsize(300,100)
root.maxsize(1200,600)


# Set the background color
root.configure(bg="lightgray")

# Create a Label
label = Label(root, text="Hello, Tkinter!", bg="lightgray", fg="black", font=("Montserrat", 16))
label.pack(pady=10)

# Create an Entry
entry = Entry(root, font=("Helvetica", 16))
entry.pack(pady=10)

# Create a Button
button = Button(root, text="Click Me", command=on_button_click, bg="lightgray", fg="black", font=("Helvetica", 16))
button.pack(pady=10)

# Run the application
root.mainloop()
