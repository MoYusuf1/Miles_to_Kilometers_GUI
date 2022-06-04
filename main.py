from tkinter import *

window = Tk()
window.title("Miles to Kilometers")


# button 1
def button_clicked():
    amount = round(int(user_input.get()) * 1.609344, 2)
    output.config(text=f"{amount}km")


# Input
user_input = Entry(width=10)
user_input.grid(row=1, column=3)

# Result
output = Label(text="Output", font=("Arial", 30, "bold"))
output.grid(row=3, column=3)

# Kilometer label
kilometer_label = Label(text="Kilometers", font=("Arial", 30, "bold"))
kilometer_label.grid(row=3, column=1)

# Equals label
equal_label = Label(text="=", font=("Arial", 24, "bold"))
equal_label.grid(row=2, column=3)

# Miles label
miles_label = Label(text="Miles", font=("Arial", 30, "bold"))
miles_label.grid(row=1, column=1)

# Button
button = Button(text="convert", command=button_clicked)
button.grid(row=4, column=2)

window.mainloop()
