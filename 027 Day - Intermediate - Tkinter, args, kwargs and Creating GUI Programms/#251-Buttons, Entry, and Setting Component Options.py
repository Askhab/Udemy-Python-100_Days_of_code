from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    my_label["text"] = input.get()


button = Button(text="Click Me", command=button_clicked)
button.pack()


# Entry
input = Entry(width=10)
input.pack()
print(input.get())


window.mainloop()
