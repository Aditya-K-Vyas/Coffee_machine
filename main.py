from data import MENU
from data import resources
# from click import clear

# TODO 1  off feature and report
def rep_off(command, res):
    if command.lower() == "off":
        print("Good Bye")
        exit(0)
    if command.lower() == "report":
        units = {
            0: "ml",
            1: "ml",
            2: "g",

        }
        dollar = "$"
        i = 0
        for resource in res:
            if i < 3:
                print(f"{resource} => {res[resource]} {units[i]}")
            else:
                print(f"{resource} =>{dollar} {res[resource]} ")
            i += 1


#  TODO 2
def are_resources_sufficient(coffee_type, res):
    i = 0
    ingredients = coffee_type["ingredients"]
    for ingredient in ingredients:
        if ingredients[ingredient] >= res[ingredient]:
            return False
    return True


def coin_processor(coffee_flavor):
    penny = int(input("How many pennies?")) * 0.01
    dime = int(input("Enter Dimes")) * 0.10
    nickel = int(input("How many pennies?")) * 0.5
    quarter = int(input("How many pennies?")) * 0.25

    total = penny + dime + nickel + quarter
    if total >= coffee_flavor['cost']:
        change = total - coffee_flavor['cost']
        print(f"Transaction successful. Your change = {change}")
        return True
    else:
        print(f"Transaction Failed. You did not enter enough money. {total} is returned to you")
        return False


while True:
    while True:
        # clear()
        user_cmd = input("Type 'off' to shutdown.\nType  'report' to get the info of resources\nType 'n' to skip  ")
        if user_cmd.lower() != 'n':
            rep_off(user_cmd, resources)
        if input("wanna continue giving admin commands? 'y' or 'n' ").lower() == 'n':
            break
    user_ch = input("What would you like ?(espresso/cappuccino/latte)")
    if user_ch.lower() == "espresso":
        coffee = MENU["espresso"]
        pass
    elif user_ch.lower() == "cappuccino":
        coffee = MENU["cappuccino"]
        pass
    elif user_ch.lower() == "latte":
        coffee = MENU["latte"]
        pass
    else:
        print("Invalid response. Do try again")
        continue
    if are_resources_sufficient(coffee, resources):
        print(f"The cost of coffee is {coffee['cost']}")
        if coin_processor(coffee):
            resources["money"] += coffee["cost"]
            #     make coffee now
            cof_ingredients = coffee["ingredients"]
            for ingredient in cof_ingredients:
                resources[ingredient] -= cof_ingredients[ingredient]
    else:
        print("Insufficient resources ")
