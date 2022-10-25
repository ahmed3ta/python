from tkinter import *
window = Tk()

def show():
    my_label.config(text=input_1.get())

window.title("My First GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

my_label = Label(text="I Am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


# Buttons


button = Button(text="Button")
button.grid(column=1, row=1)

new_button = Button(text="new Button")
new_button.grid(column=2, row=0)
# Entry

input_1 = Entry(width=30)
input_1.grid(column=4, row=3)







window.mainloop()


