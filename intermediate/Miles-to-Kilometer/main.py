import tkinter as tki

mtk_window = tki.Tk()
mtk_window.title("Miles to Kilometer Converter")
mtk_window.minsize(width=400, height=100)
mtk_window.config(padx=20, pady=20)


# Miles text box
mile_entry = tki.Entry(width=7)
# print(mile_entry.get())
mile_entry.grid(column=1, row=0)

# Miles text
miles = tki.Label(text="Miles")
miles.grid(column=2, row=0)

# Kilometers Texts
kilometers_text_left = tki.Label(text="is equal to")
kilometers_text_left.grid(column=0, row=1)

kilometers = tki.Label(text="0")
kilometers.grid(column=1, row=1)

kilometers_text_right = tki.Label(text="Kilometers")
kilometers_text_right.grid(column=2, row=1)

def mkc():
    kms = 1.60934 * int(mile_entry.get())
    kilometers.config(text=kms)

calculate_button = tki.Button(text="Calculate", command=mkc)
calculate_button.grid(column=1, row=2)


mtk_window.mainloop()