import random as rand
from py_module_stages import lives_image
from py_module_logo import logo
from py_module_wordlist import word_list

print(logo)

print("Welcome to Hangman, hope you have fun with us")

user_choice = int(input("Please select to start the game or to add to the list of words? (1 to start or 2 to add)\n"))

if user_choice == 2:
    adding_to_list = input("Please enter word now?\n").lower()
    adding_to_list.split(", ")
    word_list.append(adding_to_list)

word = rand.choice(word_list)
word_len = len(word)

letters_used = []

display = []

for letter in range(word_len):
    display += "_"

print(display)

lives = 6

end_of_game = False

while not end_of_game:

    guess = input("Please guess the letter?\n").lower()

    if guess not in word and guess not in letters_used:
        lives -= 1
        print("The letter is not within the word, you will lose the life")
        print(lives_image[lives])
        if lives == 0:
            end_of_game = True
            print("You lose")
    letters_used.append(guess)

    if guess in letters_used:
        print(f"it seems the letter {guess} you choose was already used, please attempt again!")

    for position in range(word_len):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    if guess not in word and guess not in letters_used:
        lives -= 1
        print(f"The letter {guess} is not within the word, you will lose the life")
        print(lives_image[lives])
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
