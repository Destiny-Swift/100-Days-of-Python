# Mark 1
# print(f'Your BMI is {round(float(input("Enter weight in kg: ")) / (float(input("Enter height in m: ")) ** 2), 2)}')

# Mark 2
weight = float(input('Enter weight in kg: '))
height = float(input('Enter height in m: '))
bmi = weight / height ** 2
remark = ''

if bmi < 18.5:
    remark = 'underweight and urgently in need of food'

elif bmi < 25:
    remark = 'quite normal'

elif bmi < 30:
    remark = 'slightly overweight'

elif bmi < 35:
    remark = 'obese and in need of an urgent workout'

else:
    remark = 'clinically obese and should never eat for the rest of your life'

print(f'\nWith a weight of {weight} and a height of {height}, your BMI is {round(bmi, 1)} \nYou are {remark}.')
