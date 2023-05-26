from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
## classes
fazer_cafe = CoffeeMaker()
dinheiro_maquina = MoneyMachine()
menu = Menu()

# código
is_on = True

while is_on:
    bebidas = menu.get_items()
    choice = input(f"What would you like? ({bebidas}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        fazer_cafe.report()
        dinheiro_maquina.report()
    else:
        drink = menu.find_drink(choice)
        if fazer_cafe.is_resource_sufficient(drink) and dinheiro_maquina.make_payment(drink.cost):
            fazer_cafe.make_coffee(drink)
        
