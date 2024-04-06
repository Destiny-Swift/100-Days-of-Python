import pandas as pd

nato_data = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

while True:
    def decode():

        word = input('Enter a word: ').upper()

        # if word == 'EXIT':
        #     sys.exit()

        try:
            result = [nato_dict[letter] for letter in word]
        except KeyError:
            print('Sorry, only letters in the alphabet please 🙂')
            decode()
        else:
            print(result)


    decode()
