from tkinter import *

# Function to be called when the button is clicked
def calc_area():
    print("Calculate area button called")
    r = int(txtRadius.get())
    area = 3.14 * r * r
    message = "The area of circle is " + str(area)

    lblDisplay.config(text = area)


def calc_perimeter():
    print("Calculate perimeter button called")
    r = int(txtRadius.get())
    perimeter = 2 * 3.14 * r
    message = "The perimeter of circle is " + str(perimeter)

    lblDisplay.config(text = perimeter)

    
# Create the main window
root = Tk()
root.title("Tkinter Example")
root.geometry("800x300")
root.minsize(300,100)
root.maxsize(1200,600)


# Set the background color
root.configure(bg="lightgray")

# Create a Label
lbl1 = Label(root, text="Enter the radius of circle", bg="lightgray", fg="black", font=("Montserrat", 16))
lbl1.pack(pady=10)

# Create an Entry
txtRadius = Entry(root, font=("Helvetica", 16))
txtRadius.pack(pady=10)


# Create a Button
btnArea = Button(root, text="Area", command=calc_area, bg="lightgray", fg="black", font=("Helvetica", 16))
btnArea.pack(pady=10)

btnPeri = Button(root, text="Perimeter", command=calc_perimeter, bg="lightgray", fg="black", font=("Helvetica", 16))
btnPeri.pack(pady=10)



lblDisplay = Label(root, text="", bg="lightgray", fg="black", font=("Montserrat", 16))
lblDisplay.pack(pady=10)

# Run the application
root.mainloop()
