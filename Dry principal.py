#Dry:-don't repeat yourself
import random #used for the computer choose wining own number
#wining_number=55
wining_number = random.randint(1,100) 
guess=1 
number=int(input("Guess a number between 1 to 100: "))
game_over = False

while not game_over:
	if number==wining_number:
		print(f"You win,and you guessed this number in {guess} times")
		game_over=True
	else:
		if number < wining_number :
			print("Too Low")
		else:
			print("Too High")
		guess+=1
		number=int(input("Guess again: "))