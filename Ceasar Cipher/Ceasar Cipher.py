alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(cipher_text=text, cipher_shift=shift, cipher_direction=direction):
    cipher = ""
    max_list = len(alphabet)

    for letter in cipher_text:
        position = alphabet.index(letter)
        if cipher_direction == "decode":
            new_position = position - cipher_shift
            if new_position <= 0:
                new_position = max_list + new_position
                if new_position == 26:
                    new_position = 0
                new_letter = alphabet[new_position]
                cipher += new_letter
            else:
                new_letter = alphabet[new_position]
                cipher += new_letter
        if cipher_direction == "encode":
            new_position = position + cipher_shift
            if new_position >= max_list:
                new_position = (new_position - max_list) + 0
                new_letter = alphabet[new_position]
                cipher += new_letter
            else:
                new_letter = alphabet[new_position]
                cipher += new_letter

    print(f"This is your secured message {cipher}")


caesar(cipher_text=text, cipher_shift=shift, cipher_direction=direction)
