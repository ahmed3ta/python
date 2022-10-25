import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
rps_list=[rock,paper,scissors]

user_choise_str = input("Please choose 0 for Rock, 1 for Paper, 2 for Scissors\n")
user_choise = int(user_choise_str)

computer_choise = random.randint(0,2)




if user_choise < 0 or user_choise > 2:
  print("Value Entered is not right")
elif user_choise == computer_choise:
  print(f"Computer choose:\n{rps_list[computer_choise]}")
  print(f"You choose:\n{rps_list[user_choise]}")
  print("It's a Draw")
elif (user_choise == computer_choise - 1 ) or (user_choise == 2 and computer_choise == 0):
  print(f"Computer choose:\n{rps_list[computer_choise]}")
  print(f"You choose:\n{rps_list[user_choise]}")
  print("You lose!")
elif (user_choise == computer_choise + 1) or (user_choise == 0 and computer_choise == 2):
  print(f"Computer choose:\n{rps_list[computer_choise]}")
  print(f"You choose:\n{rps_list[user_choise]}")
  print("You Win! Way to go")

