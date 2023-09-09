MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

report = {
    "resources": resources,
    "money": 0
}


is_activated = True
user_options = ['espresso', 'latte', 'cappuccino', 'off', 'report']


def subtract_resources(ingredients):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


def charge_amount(choice):
    price = choice["cost"]
    print(f'Drink costs {price}$')
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    sum = 0.00

    for coin in coins:
        amount = input(f"Choose amount of {coin} ")
        if not amount.isdigit():
            return 'Error with money.'
        amount = int(amount)
        sum += amount*coins[coin]
    if sum < price:
        print("Not enough money")
        return "didn't pay"
    else:
        if sum > price:
            print(f"Thanks for purchasing. Here is your change {sum-price}$")
        elif sum == price:
            print(f"Thanks for purchasing.")
        report["money"] += price
        return 'paid'


while is_activated:
    user_decision = input(
        'What would you like? (espresso/latte/cappuccino): ').lower()
    if user_decision not in user_options:
        print('Please pick a valid option')
    else:
        if user_decision == 'off':
            is_activated = False
            print('Thank you')
        elif user_decision == 'report':
            print(report)
        else:
            choice = MENU[user_decision]
            print(choice)
            item_needs = choice["ingredients"]
            item_misses = []
            for ingredient in item_needs:
                if item_needs[ingredient] > resources[ingredient]:
                    item_misses.append(ingredient)
            if len(item_misses) > 0:
                print(
                    f"Item is missing the following ingredient {','.join(item_misses)}")
            else:
                did_pay = charge_amount(choice)
                if did_pay == 'paid':
                    subtract_resources(choice["ingredients"])
                    print("Enjoy your coffe!")

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.


# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5


# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.


# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# Eg Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.


# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# Latte was their choice of drink.
