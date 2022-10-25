
import random
import art


#make the function that creates the attempts for the user
def attempt_choice():
	level = input(
	    "Please choose the deficulty of the game easy or hard: ").lower()
	if level == "easy":
		return 10
	elif level == "hard":
		return 5
	else:
		print("Wrong choice, we will stick with easy for now")
		return 10


#Create the random number
num = random.randint(0, 100)

print(art.logo)

#choose the number of attempts based on the diffeculty
attempt = attempt_choice()
print(f"You have {attempt} attempts")
game_over = False
while attempt > 0 and not game_over:

	guess = int(input("What is your Guess?: "))

	#Creating the logic
	if guess == num:  #if user guesses right
		game_over = True
		print(f"You Guessed right the number is {num} Congratulations")
	else:  #if user guesses wrong

		attempt -= 1  # an attempt is wasted

		#and this is to help the user, weather it's over or under his guess
		if guess > num:
			print("Too high")
		else:
			print("Too low")

		#Here to show the remainder of the attempts
		if attempt == 1:
			print(f"You have an attempt left")
		else:
			print(f"You have {attempt} attempts left")
