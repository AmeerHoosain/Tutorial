import art
import random as rand
from Data import data
from replit import clear

print(art.logo)

game_completed = False
Score = 0


def comparison(player, data_1, data_2):
    if player == "a" and data_1 > data_2:
        return 1
    elif player == "b" and data_2 > data_1:
        return 1
    elif player_choice == "a" and data_1 < data_2:
        return 2
    elif player_choice == "b" and data_1 > data_2:
        return 2



while not game_completed:
    data_len = len(data)

    option_A = rand.randint(0, data_len)
    option_B = rand.randint(0, data_len)

    first_data = data[option_A]
    second_data = data[option_B]

    if Score > 0 or first_data == second_data:
        first_data = second_data
        option_B = rand.randint(0, data_len)
        second_data = data[option_B]
        print(f"Your score is: {Score}")

    print(f"Option A: {first_data['name']}, a {first_data['description']} from {first_data['country']}")

    print(art.vs)

    print(f"Option B: {second_data['name']}, a {second_data['description']} from {second_data['country']}")

    player_choice = input("Select from the choices, which has more followers: A or B\n".lower())

    compared = comparison(player_choice, first_data['follower_count'], second_data['follower_count'])

    if compared == 1:
        Score += 1
        clear()

    else:
        print("Game Over")
        game_completed = True
