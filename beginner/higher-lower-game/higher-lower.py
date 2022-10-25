#Create a function to generate two choices (as a dictionary) from the game-data
def generate_choice():
    #import the dictionary of data and choices from random
    from game_data import data
    from random import choice
    #Create a new dictionary
    return choice(data)


#Create a function to print A if A is the higher, or B if B is the Higher
def correct_choice(a, b):
    if a['follower_count'] > b['follower_count']:
        #returns A as first in the list
        return ["A", "B"]
    else:
        #returns B as the first of the list
        return ["B", "A"]


#Generate the game function itself


def game():
    A = generate_choice()
    B = generate_choice()
    while A == B:
        B = generate_choice()
    # print(A['name'])
    # print(A['follower_count'])
    # print(B['name'])
    # print(B['follower_count'])
    correct = correct_choice(A, B)[0]
    wrong = correct_choice(A, B)[1]
    # print(correct)

    #import the ascii
    from art import logo

    game_over = False
    score = 0
    while not game_over:
        print(logo)
        print(
            f"Compare A: {A['name']}, {A['description']} from {A['country']}.")
        from art import vs
        print(vs)

        print(
            f"Against B: {B['name']}, {B['description']} from {B['country']}.")
        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        if correct == user_input:
            score += 1
            print(f"You Got it right, Your score is {score}")
            A = B
            B = generate_choice()
            while A == B:
                B = generate_choice()
        elif wrong == user_input:
            print(f"Sorry, that's wrong. Final score: {score}")
            return
        else:
            print("Wrong Choice only A or B")


game()

