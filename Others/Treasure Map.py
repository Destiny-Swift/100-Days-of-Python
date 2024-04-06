row1 = ['🌵', '🌵', '🌵']
row2 = ['🌵', '🌵', '🌵']
row3 = ['🌵', '🌵', '🌵']

treasure_map = [row1, row2, row3]

print(f'{row1}\n{row2}\n{row3}')

position = input('Where do you want to put the treasure?\n')

# there's a rule that the first digit determines the column, and you move horizontally when finding columns.
horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

# select the row with the vertical and the column with the horizontal (and column is the first input digit)
treasure_map[vertical][horizontal] = 'X'

print(f'{row1}\n{row2}\n{row3}')
