from ch16_package.coffee_maker import CoffeeMaker 
from ch16_package.menu import Menu
from ch16_package.money_machine import MoneyMachine

def start_coffee_maker():
    running = True
    coffee_menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while running:
        order = input(f"What would you like? ({coffee_menu.get_items()}): ")
        if order == "off":
            running = False
        elif order == "report":
            coffee_maker.report()
            money_machine.report()
        else :
            selected_menu = coffee_menu.find_drink(order)
            if selected_menu is None: continue
            # check if ther is enough resources &  process coin
            if (coffee_maker.is_resource_sufficient(selected_menu) 
                 and money_machine.make_payment(selected_menu.cost)): 
                coffee_maker.make_coffee(selected_menu)




if __name__ == "__main__":
    start_coffee_maker()