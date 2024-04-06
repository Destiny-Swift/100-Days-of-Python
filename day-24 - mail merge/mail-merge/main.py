# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = '[name]'

with open('Input/Names/invited_names.txt') as names:
    names = names.readlines()


for name in names:
    # making the letter
    with open('Input/Letters/starting_letter.txt') as letter:
        letter = letter.read()
        letter = letter.replace(PLACEHOLDER, name)

    # saving the letter in custom file
    with open(f"Output/ReadyToSend/Letter for {name}.doc", mode='w') as new_letter:
        new_letter.write(f'{letter}')


# Angela's method 🙄
# with open('./Input/Names/invited_names.txt') as names_file:
#     names = names_file.readlines()
#
# with open('./Input/Letters/starting_letter.txt') as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()  # apparently strip works to remove new lines 🙄
#         new_letter = letter_contents.replace(PLACEHOLDER, name)  # new variable stuff
#
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.doc", mode='w') as completed_letter:
#             completed_letter.write(f'{new_letter}')

'''
The completion of this task introduced me to useful applications of python.
This is the start of something damn great; to great and awesome!

letter has to be opened in each iteration to keep [name] constant
Or it can be opened once and a variable equated to it with each iteration of the names. (Angela's Method)
For strings, changes made to this copy variable won't affect the parent variable.
It's a different case for lists, unless you use the .copy() method.
And doc worked for MS Word extension and not docx. Hmm 🤨
'''
