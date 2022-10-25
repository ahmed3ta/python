from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ☑
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- # .


def reset_timer():
    global reps
    window.after_cancel(my_timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    text_timer.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
    check_marks.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"), highlightthickness=0)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_seconds = SHORT_BREAK_MIN * 60
    long_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_seconds)
        text_timer.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
        reps = 0
    elif reps % 2 == 0:
        count_down(short_seconds)
        text_timer.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
    else:
        count_down(work_seconds)
        text_timer.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global my_timer
    min_left = math.floor(count / 60)
    if min_left < 10:
        min_left = f"0{min_left}"
    secs_left = count % 60
    if secs_left < 10:
        secs_left = f"0{secs_left}"
    canvas.itemconfig(timer_text, text=f"{min_left}:{secs_left}")
    if count > 0:
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "☑"
        check_marks.config(text=mark, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"), highlightthickness=0)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
# window.minsize(600,300)
window.config(pady=100, padx=50, bg=YELLOW)

# Timer Text
text_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
text_timer.grid(column=1, row=0)
# Pomodoro
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(102, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Checkmarks

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"), highlightthickness=0)
check_marks.grid(column=1, row=3)

# Buttons

start_button = Button(text="Start", bg="white", highlightthickness=2, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="white", highlightthickness=2, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
