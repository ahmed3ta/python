

import random
import art
import replit



  
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def draw_card(list1):
  list1.append(random.choice(cards))
  return list1

#Acutal code

def blackjack():  
  replit.clear()
  user_deck = random.choices(cards, k=2)
  computer_deck = random.choices(cards, k=2)
  print(art.logo)
  print("Welcome to the Blackjack Game")
  print(f"Your deck has the two cards of {user_deck}\nand the computer's first card is {computer_deck[0]}")
  lose = False
  comp21 = False
  
  while not lose and input("Draw another card? y or n ") == "y" and not comp21:
    user_deck = draw_card(user_deck)
    print(f"Your deck has the two cards of {user_deck}")
    if sum(user_deck) > 21:
      lose = True
    elif sum(user_deck) == 21:
      comp21 = True
  
  
  while sum(computer_deck) < 17:
    computer_deck = draw_card(computer_deck)
    # print(f"{computer_deck}")
  
  
  
    
  if sum(user_deck) == 21:
    print(f"You have a Black jack!!\nYou win\nComputer deck is {computer_deck}")
  elif sum(computer_deck) == 21:
    print(f"computer has a Black jack!!\nYou lose\nComputer deck is {computer_deck}") 
  elif sum(user_deck) == sum(computer_deck) and not lose:
    print("it's a Dawr")
    print(f"Your's Deck is {user_deck}, and the computer deck is {computer_deck}")
  elif sum(user_deck) > sum(computer_deck) and not lose:
    print("You win")
    print(f"Your's Deck is {user_deck}, and the computer deck is {computer_deck}")
  elif sum(user_deck) < sum(computer_deck) and sum(computer_deck) < 21:
    print("You Lose")
    print(f"Your's Deck is {user_deck}, and the computer deck is {computer_deck}")
blackjack()
if input("want to play again ").lower() == "y":
  blackjack()
print ("Bye")
