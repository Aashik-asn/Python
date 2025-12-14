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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0.0
}

def check_resources(u_choice, machine, menu):
    result =[]
    for ingredient in menu[u_choice]["ingredients"]:
        if machine[ingredient] < menu[u_choice]["ingredients"][ingredient]:
            result.append(ingredient)
    if len(result)>0:
        res=",".join(result)
        return f"Insufficient Ingredients : {res}\n"
    return ""

print("COFFEE MACHINE")
print("Note: Type \"report\" to generate report of available resources")
print("      Type \"off\" to switch off the machine\n")
while True:
    transaction_status = False
    rs_check =""

    choice = input("What would you like ? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        key=list(resources.keys())
        value=list(resources.values())
        print("%s : %sml"%(key[0],value[0]))
        print("%s : %sml"%(key[1],value[1]))
        print("%s : %sg"%(key[2],value[2]))
        print("%s : $%s\n"%(key[3],value[3]))
        continue
    elif choice == "off":
        print("Thank you!!❤️")
        break
    elif choice == "espresso":
        rs_check = check_resources(choice, resources, MENU)
    elif choice == "latte":
        rs_check = check_resources(choice, resources, MENU)
    elif choice == "cappuccino":
        rs_check = check_resources(choice, resources, MENU)
    else:
        print("Invalid Input....Try Again !!!")
        continue

    if rs_check=="":
        print("\nInsert Coin in the format(quarters dimes nickles pennies): ")
        insert_coin=input("Eg: \"1 2 1 2\" which means 1 quarter 2 dimes "
                          "1 nickles and 2 pennies\n").split()
        user_amount=(int(insert_coin[0])*0.25 + int(insert_coin[1])*0.10
                    + int(insert_coin[2])*0.05 + int(insert_coin[3])*0.01)
        user_amount=round(user_amount,2)
        if MENU[choice]["cost"]==user_amount:
             resources["Money"]=user_amount
             transaction_status=True
        elif MENU[choice]["cost"]<user_amount:
            resources["Money"]=MENU[choice]["cost"]
            transaction_status=True
            change=user_amount-MENU[choice]["cost"]
            print(f"Here is ${change:.2f} dollars in change")
        else:
            print("Sorry that's not enough money. Money refunded.\n")
    else:
        print(rs_check)
    if transaction_status:
        print(f"Thanks for ordering!!! Here is your {choice}\n")
        resources["water"]-=MENU[choice]["ingredients"].get("water",0)
        resources["milk"]-=MENU[choice]["ingredients"].get("milk",0)
        resources["coffee"]-=MENU[choice]["ingredients"].get("coffee",0)
