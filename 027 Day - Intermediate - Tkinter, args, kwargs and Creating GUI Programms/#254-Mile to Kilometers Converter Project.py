from tkinter import *


def calculate():
    miles = float(input_miles.get())
    km = miles * 1.609
    label_km_num["text"] = f"{km}"


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Labels
label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_km_num = Label(text="0")
label_km_num.grid(column=1, row=1)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_kms = Label(text="Km")
label_kms.grid(column=2, row=1)

# Entry
input_miles = Entry(width=7)
input_miles.grid(column=1, row=0)


# Button
button_calculate = Button(text="Calculate", command=calculate)
button_calculate.grid(column=1, row=2)


window.mainloop()
