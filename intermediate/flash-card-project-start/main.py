from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# Generate random German word


def flip():
    word_window.itemconfig(window_image, image=canvas_image_front)
    word_window.itemconfig(my_title, text="English", fill="black")
    word_window.itemconfig(my_word, text=word["English"], fill="black")


def random_word():
    global word
    global flipping
    word_window.after_cancel(flipping)
    word_window.itemconfig(window_image, image=canvas_image_back)
    word = random.choice(data)
    word_window.itemconfig(my_title, text="German", fill="white")
    word_window.itemconfigure(my_word, text=word["German"], fill="white")
    flipping = word_window.after(3000, flip)


def known_word():
    random_word()
    data.remove(word)
    print(len(data))
    pandas.DataFrame(data).to_csv("data/words_to_learn.csv.csv", index=False)


def unknown_word():
    random_word()

# Main Window


flashy = Tk()
flashy.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


# Canvas of the flash cards
word_window = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image_back = PhotoImage(file="images/card_back.png")
canvas_image_front = PhotoImage(file="images/card_front.png")
window_image = word_window.create_image(400, 263, image=canvas_image_back)

try:
    data_dataframe = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    data_dataframe = pandas.read_csv("data/german-to-english.csv")

data = data_dataframe.to_dict(orient="records")

word = random.choice(data)

my_title = word_window.create_text(400, 150, text="German", font=("Arial", 40, "bold"), fill="white")
my_word = word_window.create_text(400, 263, text=word["German"], font=("Arial", 60, "bold"), fill="white")
word_window.grid(column=0, row=0, columnspan=2)

# Buttons

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=2, command=known_word)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_image, highlightthickness=2, command=unknown_word)
wrong_button.grid(column=0, row=1)

flipping = word_window.after(3000, flip)

flashy.mainloop()
