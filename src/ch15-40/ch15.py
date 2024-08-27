"""=== Coffee Machine ==="""

resources = {
    "Water":300,
    "Milk":200,
    "Coffee":100
}

profit = 0

MENU = {
        "espresso": { 
            "ingredients":{"Water":50, "Milk":0, "Coffee":18},
            "cost":1.5
        },
        "latte": {
            "ingredients":{"Water":200, "Milk":150, "Coffee":24},
            "cost":2.5
        },
        "cappuccino": {
            "ingredients":{"Water":250, "Milk":100, "Coffee":24},
            "cost":3
        }
    }

def print_report():
    print(f"Water: {resources['Water']}ml")
    print(f"Milk: {resources['Milk']}ml")
    print(f"Coffee: {resources['Coffee']}g")
    print(f'Money: ${"{:.2f}".format(profit)}')

def process_coins():
    print("Please insert coins")
    total=int(input("How many quarters?: "))*0.25
    total+=int(input("How many dimes?: "))*0.10
    total+=int(input("How many nickles?: "))*0.05
    total+=int(input("How many pennies?: "))*0.01
    return total
    
def check_ingredients(ingredients):
    for key in ingredients:
        if resources[key] < ingredients[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

def make_coffee(coffee_menu:str):
    coffee = MENU[coffee_menu]
    if check_ingredients(coffee["ingredients"]):
        received_money = process_coins()
        if received_money < coffee["cost"]:
            print(f"Sorry that's not eunough money. Money refunded.")
        else:
            for key in coffee["ingredients"]:
                resources[key] -= coffee["ingredients"][key]

            global profit
            profit += coffee["cost"]
            change = received_money - coffee["cost"]
            print(f"Here is ${"{:.2f}".format(change)} in change.")
            print(f"Here is your {coffee_menu} Enjoy!")
    

commands_function = {
    "off":exit,
    "report":print_report,
    "espresso": lambda: make_coffee("espresso"),
    "latte": lambda: make_coffee("latte"),
    "cappuccino": lambda: make_coffee("cappuccino")
}


def start_coffee_machines():
    while True:
        command = input("What would you like? (espresso/latte/cappuccino): ")
        commands_function[command]()

if __name__ == "__main__":
    start_coffee_machines()