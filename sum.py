from tkinter import *

# Function to be called when the button is clicked
def on_button_click():
    print("Button clicked!")
    num1 = int(txt1.get())
    num2 = int(txt2.get())
    total = num1 + num2

    label.config(text = total)

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
txt1 = Entry(root, font=("Helvetica", 16))
txt1.pack(pady=10)

txt2 = Entry(root, font=("Helvetica", 16))
txt2.pack(pady=10)


# Create a Button
button = Button(root, text="Click Me", command=on_button_click, bg="lightgray", fg="black", font=("Helvetica", 16))
button.pack(pady=10)

# Run the application
root.mainloop()
