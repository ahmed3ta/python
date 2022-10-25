from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the Blind Oction Program")
exit_program = False
dictionary_of_bidders = {}
while not exit_program:
  bidder = input("What is your Name?\n")
  bid = int(input("what is your bid? \n$"))
  dictionary_of_bidders[bidder] = bid

  new_bidder = input("Is there another Bidder? \ntype 'yes' or 'no'\n").lower()
  if new_bidder == "no" or "n":
    exit_program = True
  clear()

# print(dictionary_of_bidders)
highest_pid = 0
highest_pider = ""
for key in dictionary_of_bidders:
  if highest_pid < dictionary_of_bidders[key]:
    highest_pid = dictionary_of_bidders[key]
    highest_pider = key

print(f"The Highest Bidder is {highest_pider} with a Bid of {highest_pid}")
  
  
