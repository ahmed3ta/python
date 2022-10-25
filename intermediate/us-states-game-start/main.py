import turtle
import pandas
from state_create import StateCoorCreate

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

state_data = pandas.read_csv("50_states.csv")

guessed_count = 0
game_is_on = True
guessed_answers = []
while game_is_on:

    answer_state = screen.textinput(title=f"{guessed_count}/50 Guess the State", prompt="What is a state name?").title()
    if answer_state == "Exit":
        break
    for state in state_data["state"]:
        if answer_state == state:
            if state not in guessed_answers:
                guessed_answers.append(answer_state.title())
                guessed_count = len(guessed_answers)
                # print(guessed_answers)

                x_cor = int(state_data[state_data.state == state].x)
                y_cor = int(state_data[state_data.state == state].y)
                new_state = StateCoorCreate(x_cor, y_cor, state)
                # print(x_cor)

# states_to_learn.csv
states_missed = {}
#
# for state in state_data["state"]:
#     if state not in guessed_answers:
#         states_missed["States to learn"].append(state)
states_missed["States to learn"] = [s for s in state_data["state"] if s not in guessed_answers]


states_missed_data = pandas.DataFrame(states_missed)
states_missed_data.to_csv("states_to_learn.csv")
print(states_missed)
# screen.exitonclick(states_to_learn.csv)
