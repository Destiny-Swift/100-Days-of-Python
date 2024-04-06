from caesar_cipher_art import logo
print(logo)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    for char in start_text.lower():
        if char in alphabets:
            position = alphabets.index(char)

            if cipher_direction == 'decode':
                shift_amount *= -1  # shortens required code lines (take sometime on it)

            new_position = position + shift_amount  # negative indexing was really a lifesaver here (for deciphering)
            new_position %= 26

            end_text += alphabets[new_position]

        else:
            end_text += char

    end_text = list(end_text)

    for position in range(len(end_text)):  # capitalise every capitalised position in the initial text
        if start_text[position].isupper():
            end_text[position] = end_text[position].upper()

    print(f"\nThe {cipher_direction}d text is \n\t{''.join(end_text)}")


should_continue = True

while should_continue:
    operation = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input('Type your message:\n')
    shift = int(input('Type the shift number:\n'))
    alphabets = list("abcdefghijklmnopqrstuvwxyz")  # smart way of making a list of alphabets

    caesar(start_text=text, shift_amount=shift, cipher_direction=operation)

    feedback = input("\n\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
    if feedback == 'no':
        should_continue = False
        print('Goodbye')
