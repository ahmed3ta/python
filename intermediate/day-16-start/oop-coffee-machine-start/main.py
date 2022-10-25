from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()

is_on = True
while is_on:
    user_input = input(f"What would you like? ({my_menu.get_items()}):")

    if user_input == "off":
        is_on = False
    elif user_input == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        my_menu_item = my_menu.find_drink(user_input)
        if my_coffee_maker.is_resource_sufficient(my_menu_item) and my_money_machine.make_payment(my_menu_item.cost):
            my_coffee_maker.make_coffee(my_menu_item)
