from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# initiate dependencies (just some big grammar 🙄)
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


machine_is_working = True  # the flag
while machine_is_working:
    print(f'What would you like? ({menu.get_items()})', end='')
    prompt = input(': ')

    if prompt == 'off':
        print('Good Bye!')
        machine_is_working = False

    elif prompt == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(prompt)

        if drink in menu.menu:  # first check if drink is in the menu
            if coffee_maker.is_resource_sufficient(drink):  # and then check if resource for drink is sufficient
                if money_machine.make_payment(drink.cost):  # and then check if payment is successful
                    coffee_maker.make_coffee(drink)  # make the fucking coffee

# Alternatively you could combine all 3 if statements in one with an 'ANDs'
# Done with this shit. Now this is how we roll.
