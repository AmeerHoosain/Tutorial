from Art import logo
from menu import MENU

print(logo)

coffee_mug = "☕"

power_up = True

water = 1000
milk = 500
coffee = 150
money = 0

while power_up:

    user_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    if user_choice == "report":
        print(f"""
            water   : {water}ml
            milk    : {milk}ml
            coffee  : {coffee}g
            Money   : R{money}
        """)

    if user_choice == "refill":
        if 0 < water < 50:
            water = 1000
        elif 0 < milk < 50:
            milk = 500
        elif 0 < coffee < 18:
            coffee = 150

    if user_choice == "off":
        power_up = False

    if user_choice == "latte" or user_choice == "cappuccino" or user_choice == "espresso":
        recipe = MENU[user_choice]
        recipe_preing = recipe["ingredients"]
        recipe_milk = recipe_preing["milk"]
        recipe_water = recipe_preing["water"]
        recipe_coffee = recipe_preing["coffee"]
        print("Please insert coins")
        coin_check_quarters = int(input("How much quarters?\n"))
        coin_check_dimes = int(input("How much dimes?\n"))
        coin_check_nickles = int(input("How much nickles?\n"))
        coin_check_pennies = int(input("How much pennies?\n"))
        Total = float((coin_check_pennies * 0.25) + (coin_check_dimes * 0.10) + (coin_check_nickles * 0.05) + (
                coin_check_pennies * 0.01))
        Total_amount = round(Total, 2)
        if Total_amount >= recipe["cost"]:
            change = round(Total_amount - recipe["cost"], 2)
            print(f"Total inserted money: ${Total_amount}, your change will be ${change}")
            if recipe["cost"] > Total_amount:
                print(f"Sorry, but you gave to little money, refund {Total_amount}")
            elif recipe_milk > milk or recipe_coffee > coffee or recipe_water > water:
                print(
                    f"We apologize for the inconvenience, your money will be refunded, total ${Total_amount}, please "
                    f"refill")
            else:
                milk -= recipe_milk
                coffee -= recipe_coffee
                water -= recipe_water
                money += recipe["cost"]
                print(
                    f"Thank you for your purchase, please remove your {coffee_mug}{user_choice} and enjoy your day "
                    f"further")
                print(f"Please remember to take your change: ${change}")
