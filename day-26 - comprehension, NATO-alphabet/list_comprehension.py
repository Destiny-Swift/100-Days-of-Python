# LIST COMPREHENSION

# squared_numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Do Not Change the code above 👆

# Write your 1 line of code below:
squared_numbers = [number ** 2 for number in numbers]
# Write your code above:

print(squared_numbers)

# even numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Do not change the code above 👆

# Write your 1 line code below:
result = [number for number in numbers if number % 2 == 0]
# Write your 1 line code above:

print(result)


# common numbers

results = [int(number) for number in open('file1.txt').read().split('\n')
           if number in open('file2.txt').read().split('\n')]  # Dang PEP
# Write your code above 👆

print(results)
