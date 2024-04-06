students_score = [81, 71, 69, 91, 82, 90]

highest_score = 0
for score in students_score:
    if score > highest_score:
        highest_score = score

print(f'The highest score in th class is: {highest_score}')
