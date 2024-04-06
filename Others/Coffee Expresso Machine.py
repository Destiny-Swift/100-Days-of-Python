menu = {
    'expresso': {'water': 50, 'coffee': 18, 'milk': 0, 'price': 1.50},
    'latte': {'water': 200, 'coffee': 24, 'milk': 150, 'price': 2.50},
    'cappuccino': {'water': 250, 'coffee': 24, 'milk': 100, 'price': 3.00}
}

resources = {'water': 300, 'milk': 200, 'coffee': 100, 'money': 0}


def check_resources(flavor):
    ingredients = ['water', 'coffee', 'milk', 'money']
    for ingredient in ingredients:
        if menu[flavor][ingredient] > resources[ingredient]:
            return f"Sorry there is not enough {ingredient}"
        return 'okay'


def check_money(flavor, money):
    """Returns 'okay' if the money is sufficient or an insufficient money message when the money is not sufficient."""
    cost = menu[flavor]['price']
    if cost > money:
        return "Sorry, that's not enough money. Money refunded."
    return 'okay'


def collect_coins():
    """Returns the total amount in dollars of the coins inserted."""
    print('Please insert coins')
    quarters = int(input('How many quarters: '))
    dimes = int(input('How many dimes: '))
    nickels = int(input('How many nickels: '))
    pennies = int(input('How many pennies: '))

    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)


def make_coffee(flavor):
    resources['water'] -= menu[flavor]['water']
    resources['milk'] -= menu[flavor]['milk']
    resources['coffee'] -= menu[flavor]['coffee']
    resources['money'] += menu[flavor]['price']  # add the money to the account 🤑


while True:
    choice = input('What would you like? (expresso/latte/cappuccino): ')

    if choice == 'off':
        break

    elif choice == 'report':
        print(f"""
        Milk: {resources['milk']}ml
        Water: {resources['water']}ml
        Coffee: {resources['coffee']}g
        Money: ${resources['money']}
        \n""")

    elif choice == 'expresso' or choice == 'latte' or choice == 'cappuccino':
        if check_resources(choice) == 'okay':
            payment = collect_coins()

            if check_money(choice, payment) == 'okay':
                change = round(payment - menu[choice]['price'], 2)

                make_coffee(choice)
                print(f"""
                Here is ${change} in change.
                Here is your {choice} ☕ Enjoy!
                """)

            else:
                print(check_money(choice, payment))
        else:
            print(check_resources(choice))


# 3 flavors
# Expresso ($1.50) - 50ml water, 18g coffee, 0ml milk
# Latte ($2.50) - 200ml water, 24g coffee, 150ml milk
# Cappuccino ($3.00) - 250ml water, 24g coffee, 100ml milk


# print resources status report

# check that resources are sufficient when the user orders a drink or return their money back to them.


# Take input from the user; what coffe they would like, exit, or print resource status report
# print report or exit if that's requested. Ask user for coins if they choose any of the 3 flavors of coffee
# How many quarters, dimes, nickels and pennies?
# Give them change (if any, although would most times be the case)
# Give them their {whatever flavor they order coffee, fix in some hot coffee emoji and ask them to enjoy.😋
# When resources aren't enough to prepare chosen drink, let the user know, with some wonderful message that lets them
# know about all the resources that aren't enough
# Refund the user when the isn't enough
# Check whether transaction is successful - basically when the user puts in enough coins, and then proceed to make the
# drink
