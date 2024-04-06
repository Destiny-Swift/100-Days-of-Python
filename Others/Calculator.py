from calculator_art import logo


def add(n1, n2):  # addition
    return n1 + n2


def subtract(n1, n2):  # subtract
    return n1 - n2


def multiply(n1, n2):  # multiple
    return n1 * n2


def divide(n1, n2):  # divide
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)

    digit_1 = float(input("What's the first number?: "))

    continue_calculation = True

    while continue_calculation:
        for operation in operations:
            print(operation)

        operation =input('Pick an operation: ')

        digit_2 = float(input("What's the second number?: "))

        calculation_function = operations[operation]
        result = calculation_function(digit_1, digit_2)

        print(f'{digit_1} {operation} {digit_2} = {result}')

        feedback = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if feedback == 'n':
            calculator()

        else:
            digit_1 = result


calculator()
