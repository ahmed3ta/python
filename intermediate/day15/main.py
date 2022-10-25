from components import MENU


def report(log_entry):
    """This Function takes the log list, and print the values of the latest log"""
    # Initial amount of resources is
    # Water: 1000ml
    # Milk: 500ml
    # Coffee: 200g
    # Money: $2.5

    n = -1
    latest = list(log_entry)[n]
    entry = log_entry[latest]['ingredients']
    print(f"change: {log_entry[latest]['change']}$")

    for i in entry:
        if i == "milk" or i == "water":
            print(f"{i}: {entry[i]}ml")
        else:
            print(f"{i}: {entry[i]}g")
    while "milk" not in entry:
        n -= 1
        latest = list(log_entry)[n]
        entry = log_entry[latest]['ingredients']
        print(f"milk: {entry['milk']}ml")

    # print(f"Water: {log_entry[latest]['ingredients']['water']}ml")
    # print(f"Milk: {log_entry[latest]['ingredients']['milk']}ml")
    # print(f"Coffee: {log_entry[latest]['ingredients']['coffee']}g")
    # print(f"Money: {log_entry[latest]['change']}$")


# TODO: 4. check if the resources are sufficient for the order


def ingredients_enough(choice, log_entry):
    latest = list(log_entry)[-1]
    machine_data = log_entry[latest]["ingredients"]
    choice_data = MENU[choice]["ingredients"]
    sufficient = True
    for i in choice_data:
        if machine_data[i] < choice_data[i]:
            sufficient = False
    return sufficient

# TODO: 3. create a log list to track down choices


def enter_money():

    # TODO: 5. process coins
    # quarters = $0.25,
    # dimes = $0.10,
    # nickles = $0.05,
    # pennies = $0.01
    amount = float(input("quarters: ")) * 0.25
    amount += float(input("dimes: ")) * 0.10
    amount += float(input("nickles: ")) * 0.05
    amount += float(input("pennies: ")) * 0.01
    return amount


def add_to_log(log_entry, choice, money, turns):
    n = -1
    latest = list(log_entry)[n]
    log_1 = f'{choice}-{str(turns)}'
    log_entry[log_1] = {
        "ingredients": {},
        "change": 0
    }
    for key in MENU[choice]["ingredients"]:
        log_entry[log_1]["ingredients"][key] = log_entry[latest]["ingredients"][key] - MENU[choice]["ingredients"][key]
    if"milk" not in MENU[choice]["ingredients"]:
        n -= 1
        latest = list(log_entry)[n]
        log_entry[log_1]["ingredients"]["milk"] = log_entry[latest]["ingredients"]["milk"]
    log_entry[log_1]["change"] = round(money - MENU[choice]["cost"], 2)


log = {
    "initial": {
        "ingredients": {
            "water": 1000,
            "milk": 500,
            "coffee": 200,
        },
        "change": 0.0
    }
}


def coffee_machine():
    rounds = 0
    off = False
    while not off:
        # TODO: 1. Get the user input from a list of components

        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO: 2. turn off when "off" is inputted, and print a report when the user chooses report

        if user_input == "off":
            off = True
        elif user_input == "report":
            report(log)
        else:
            if user_input not in MENU:
                print("Wrong input, please enter a valid option")
            elif ingredients_enough(user_input, log):
                user_money = round(enter_money(), 2) + log[list(log)[-1]]["change"]
                choice_money = MENU[user_input]["cost"]
                print(user_money)
                print(choice_money)
                # TODO: 6. check the transaction is successful
                if user_money >= choice_money:
                    # TODO: 7. make the coffee
                    add_to_log(log, user_input, user_money, rounds)
                    print(log)
                    rounds +=1
                else:
                    print("insufficient Money for your order")
            else:
                print("Insufficient ingredients")
                # latest = list(log)[-1]
                # machine_data = log[latest]["ingredients"]
                # choice_data = MENU[user_input]["ingredients"]
                # for ing in machine_data:
                #     if machine_data[ing] < choice_data[ing]:
                #         print(f"Sorry, insufficient {ing}")


coffee_machine()








