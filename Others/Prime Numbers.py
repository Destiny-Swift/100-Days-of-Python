# A prime number checker

def prime_checker(number):
    is_true = True
    for i in range(2, number):
        if number % i == 0:
            is_true = False

    if is_true:
        print('It\'s a prime number')
    else:
        print('It\'s not a prime number')


n = int(input('Check this number: '))
print(prime_checker(number=n))
