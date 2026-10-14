resources = {"water": 300, "milk": 200, "coffee": 100}

MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}


def report():
    """Print the machine's remaining resources."""
    for item, amount in resources.items():
        print(f"{item}: {amount}")


def is_resource_sufficient(ingredients):
    """Return True if there is enough of every ingredient, else say what is missing."""
    for item, amount in ingredients.items():
        if amount > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def make_coffee(drink_name, ingredients):
    """Use up the ingredients and serve the drink."""
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name}. Enjoy!")


machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        report()
    else:
        drink = MENU.get(choice)
        if drink is None:
            print("Sorry, that's not on the menu.")
        elif is_resource_sufficient(drink["ingredients"]):
            print(f"That will be £{drink['cost']:.2f}.")
            payment = float(input("How much are you paying? £"))
            if payment >= drink["cost"]:
                change = round(payment - drink["cost"], 2)
                print(f"Here is £{change:.2f} in change.")
                make_coffee(choice, drink["ingredients"])
            else:
                print("Sorry, that's not enough money. Money refunded.")
