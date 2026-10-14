"""Solutions to the Week 4 extra practice projects.
Run this file and choose Banker Roulette, Password Generator, Blind Auction,
or Coffee Machine from the menu.
"""
import random
import string


def banker_roulette():
    """Choose a payer using both random.choice and random.randint."""
    friends = ["Alice", "Bob", "Charlie", "Dana", "Ella"]

    payer = random.choice(friends)
    print(f"Version 1: {payer} is paying the bill today!")

    num_friends = len(friends)
    index = random.randint(0, num_friends - 1)
    payer = friends[index]
    print(f"Version 2: {payer} is paying the bill today!")


def ask_non_negative_int(prompt):
    """Ask for a whole number that is zero or greater."""
    while True:
        try:
            answer = int(input(prompt))
            if answer < 0:
                print("Please enter 0 or a positive whole number.")
                continue
            return answer
        except ValueError:
            print("Please enter a whole number, such as 8.")


def password_generator():
    """Generate easy-order and shuffled passwords from requested character counts."""
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = ask_non_negative_int("How many letters would you like? ")
    nr_symbols = ask_non_negative_int("How many symbols would you like? ")
    nr_numbers = ask_non_negative_int("How many numbers would you like? ")

    # Easy version: letters, then symbols, then numbers.
    password = ""
    for _ in range(nr_letters):
        password += random.choice(letters)
    for _ in range(nr_symbols):
        password += random.choice(symbols)
    for _ in range(nr_numbers):
        password += random.choice(numbers)
    print(f"Easy version: {password}")

    # Hard version: create a list and shuffle its characters before joining.
    password_list = []
    for _ in range(nr_letters):
        password_list.append(random.choice(letters))
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Shuffled version: {password}")


def blind_auction():
    """Collect private bids and print only the winning bidder and bid."""
    bids = {}
    keep_bidding = True
    while keep_bidding:
        name = input("What is your name? ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        try:
            bid = int(input("What is your bid in pounds? £"))
            if bid < 0:
                print("Bid cannot be negative.")
                continue
        except ValueError:
            print("Please enter the bid as a whole number.")
            continue
        bids[name] = bid
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
        if other_bidders == "no":
            keep_bidding = False
        else:
            print("\n" * 100)

    highest_bid = -1
    winner = ""
    for name, bid in bids.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = name
    if winner:
        print(f"The winner is {winner} with a bid of £{highest_bid}.")
    else:
        print("No bids were entered.")


def coffee_machine():
    """Run the menu-driven coffee machine with finite resources and payment."""
    resources = {"water": 300, "milk": 200, "coffee": 100}
    menu = {
        "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
        "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
        "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
    }

    def report():
        """Print the amount of each resource remaining."""
        for item, amount in resources.items():
            unit = "ml" if item in ("water", "milk") else "g"
            print(f"{item}: {amount}{unit}")

    def is_resource_sufficient(ingredients):
        """Return whether the machine has all ingredients required for a drink."""
        for item, amount in ingredients.items():
            if amount > resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_coffee(drink_name, ingredients):
        """Deduct drink ingredients and confirm the drink is ready."""
        for item, amount in ingredients.items():
            resources[item] -= amount
        print(f"Here is your {drink_name}. Enjoy!")

    machine_on = True
    while machine_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if choice == "off":
            machine_on = False
        elif choice == "report":
            report()
        else:
            drink = menu.get(choice)
            if drink is None:
                print("Sorry, that's not on the menu.")
                continue
            if not is_resource_sufficient(drink["ingredients"]):
                continue
            cost = drink["cost"]
            print(f"That will cost £{cost:.2f}.")
            try:
                payment = float(input("How much are you paying? £"))
            except ValueError:
                print("Invalid amount. Money refunded.")
                continue
            if payment >= cost:
                change = round(payment - cost, 2)
                print(f"Here is your change: £{change:.2f}")
                make_coffee(choice, drink["ingredients"])
            else:
                print("Sorry, that's not enough money. Money refunded.")


def main():
    """Let the user select which extra practice project to run."""
    choices = {
        "1": ("Banker Roulette", banker_roulette),
        "2": ("Password Generator", password_generator),
        "3": ("Blind Auction", blind_auction),
        "4": ("Coffee Machine", coffee_machine),
    }
    print("Week 4 Extra Practice Projects")
    print("1. Banker Roulette")
    print("2. Password Generator")
    print("3. Blind Auction")
    print("4. Coffee Machine")
    choice = input("Choose a project (1-4): ").strip()
    selected = choices.get(choice)
    if selected is None:
        print("Please run the file again and choose 1, 2, 3, or 4.")
        return
    print(f"--- {selected[0]} ---")
    selected[1]()


if __name__ == "__main__":
    main()
