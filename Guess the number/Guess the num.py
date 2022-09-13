
from logo import Logo
import random as rand


print(Logo)
print("Welcome to Guess the number game")
print("Guess a number between 1 and 100!")
difficulty = input("To begin, please select the difficulty? 'easy' or 'hard'\n".lower())
if difficulty == "hard":
    choice_lives = 5
else:
    choice_lives = 10

lives = choice_lives

rand_number = rand.randint(1, 100)

game_completed = False


def game_mech(number, user_choice):
    if number > user_choice:
        return 1
    elif number < user_choice:
        return 2
    elif number == user_choice:
        return 3


while not game_completed:
    user_input = int(input("Lets start by guessing the number:\n"))
    if user_input in range(1,101):
        if game_mech(rand_number, user_input) == 1:
            if lives > 0:
                print("The number is too low!")
                lives -= 1
                print(lives)
            else:
                game_completed = True
                print(rand_number)
        elif game_mech(rand_number, user_input) == 2:
            if lives > 0:
                print("The number is too high!")
                lives -= 1
                print(lives)
            else:
                game_completed = True
                print(rand_number)
        elif game_mech(rand_number, user_input) == 3:
            print("congrats you found the number")
            game_completed = True
            print(rand_number)
    else:
        print("incorrect number, please select 1 - 100")
