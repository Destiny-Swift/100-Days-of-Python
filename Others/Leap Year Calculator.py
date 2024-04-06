# Leap Year Calculator
while True:
    year = int(input('Enter the year: '))

    # if year % 4 == 0:
    #     if year % 100 == 0:
    #         if year % 400 == 0:
    #             print('Leap year')
    #         else:
    #             print('Not a leap year')
    #     else:
    #         print('Leap year')
    # else:
    #     print('Not a leap year')

    # Mark 2
    if (year % 4 == 0 or year % 100 == 0) and (year % 400 == 0):
        print('Leap year')
    else:
        print('Not a leap year')
