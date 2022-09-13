import random as rand

import replit

import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = rand.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def check_score(player, computer):
    if player > 21 and computer > 21:
        return "You lose"
    if player == computer:
        return "Its a draw!"
    elif player == 21 or player == 0:
        return "You win! BlackJack"
    elif computer == 21 or computer == 0:
        return "Computer wins! BlackJack"
    elif player > 21:
        return "You went bust!"
    elif computer > 21:
        return "Computer went bust!"
    elif player > computer:
        return "You win"
    elif computer > player:
        return "Computer win"


def play_game():
    print(art.logo)

    player_cards = []
    computer_cards = []
    game_done = False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_done:

        player_score = calculate_score(cards=player_cards)
        computer_score = calculate_score(cards=computer_cards)
        print(f"Your cards: {player_cards}, your current score is {player_score}")
        print(f"The computer's first cards is {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_done = True
        else:
            hit = input("Would you like to hit?\n")
            if hit == "y":
                player_cards.append(deal_card())
            else:
                game_done = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final score is {player_score}")
    print(f"Computer score is {computer_score}")
    print(check_score(player=player_score, computer=computer_score))

    game_completion = input("Would you like to play game of BlackJack? y or n\n".lower())
    if game_completion == "y":
        replit.clear()
        play_game()


play_game()
