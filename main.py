QUARTERS = 0.25
NICKELS = 0.05
DIMES = 0.10
PENNIES = 0.01

resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }

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


def report(resources):
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffe: {resources['coffee']}\n"
          f"Money: ${resources['money']}")


def prompt(drink):
    return drink


def resource_spend(prompt, resources):
    if prompt != "espresso":
        resources["water"] -= MENU[prompt]["ingredients"]["water"]
        resources["milk"] -= MENU[prompt]["ingredients"]["milk"]
        resources["coffee"] -= MENU[prompt]["ingredients"]["coffee"]
    elif prompt == "espresso":
        resources["water"] -= MENU[prompt]["ingredients"]["water"]
        resources["coffee"] -= MENU[prompt]["ingredients"]["coffee"]


def check_resources(prompt, resources):
    if prompt != "espresso" and resources["water"] >= MENU[prompt]["ingredients"]["water"]:
        if resources["milk"] >= MENU[prompt]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU[prompt]["ingredients"]["coffee"]:
                return True

    elif prompt == "espresso" and resources["water"] >= MENU[prompt]["ingredients"]["water"]:
        if resources["coffee"] >= MENU[prompt]["ingredients"]["coffee"]:
            return True

    if resources["water"] <= MENU[prompt]["ingredients"]["water"]:
        print("Sorry, there is not enough water 😢")
        return False
    if prompt != "espresso" and resources["milk"] <= MENU[prompt]["ingredients"]["milk"]:
        print("Sorry, there is not enough milk 😢")
        return False
    if resources["coffee"] <= MENU[prompt]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee 😢")
        return False


def process_coins(drink, resources):
    print("Please insert coins.")
    quarters_amount = int(input("How many quarters? "))
    dimes_amount = int(input("How many dimes? "))
    nickels_amount = int(input("How many nickles "))
    pennies_amount = int(input("How many pennies? "))

    coins_sum = quarters_amount * QUARTERS \
                + dimes_amount * DIMES + \
                nickels_amount * NICKELS \
                + pennies_amount * PENNIES \

    change = coins_sum - MENU[drink]["cost"]

    if coins_sum == MENU[drink]["cost"]:
        resources["money"] += coins_sum
        return drink
    elif coins_sum > MENU[drink]["cost"]:
        resources["money"] += round(coins_sum - change, 2)
        return f"Here is your ${round(change, 2)} in change.\nHere is your {drink}. Enjoy! ☕️"
    else:
        return "Not enough coins"


def coffee_machine():
    is_machine_on = True

    while is_machine_on:
        choice = input("What would you like to drink? (espresso/latte/cappuccino)? ")
        drink = prompt(choice)

        if choice == "off":
            is_machine_on = False

        elif choice == "report":
            report(resources)

        elif check_resources(drink, resources):
            result = process_coins(drink, resources)
            if result == "Not enough coins":
                print(result)
                continue
            else:
                print(result)
                resource_spend(drink, resources)


coffee_machine()



