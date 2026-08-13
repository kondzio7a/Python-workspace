import numpy as np

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
}

def choose_coffee():
    while True:
        print("Welcome to the coffee machine!\n 1 - Espresso\n 2 - Latte\n 3 - Cappuccino")
        choice = int(input("Please choose a coffee:"))
        if choice == 1:
            print(f"You have to pay {MENU["espresso"]["cost"]} zł")
            cost = np.float32(MENU["espresso"]["cost"])
            return cost
        elif choice == 2:
            print(f"You have to pay {MENU["latte"]["cost"]} zł")
            cost = np.float32(MENU["latte"]["cost"])
            return cost
        elif choice == 3:
            print(f"You have to pay {MENU["cappuccino"]["cost"]}zł")
            cost = np.float32(MENU["cappuccino"]["cost"])
            return cost
        else:
            print("Please choose a coffee")

def money(zl = 0,gr = 0):
    zl = np.float32(input("Type how many zloty's you want to add"))
    gr = np.float32(input("Type how many groszy's you want to add"))
    price = round(zl+(gr*0.01),2)
    return price

cena = choose_coffee()
kasa = money()

print(f"Your check {round(kasa - cena,2)} zł")