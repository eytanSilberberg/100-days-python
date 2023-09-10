from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
resources = coffee_maker.resources
money_machine = MoneyMachine()
while is_on:
    choice = input(f'What would you like to drink? choose one of the options: {menu.get_items()}').lower()
    if choice == 'off':
        print('Ok bye')
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(choice)
        if item:
            if coffee_maker.is_resource_sufficient(item):
                price = item.cost
                is_enough_money = money_machine.make_payment(price)
                if is_enough_money:
                    coffee_maker.make_coffee(item)
