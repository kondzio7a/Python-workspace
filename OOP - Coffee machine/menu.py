class AvaiableCoffee:
    def __init__(self, name, price, water, milk, coffee):
        self.name = name
        self.price = price
        self.ingredients = {
            "milk": milk,
            "coffee": coffee,
            "water": water
        }


class Menu:
    def __init__(self):
        self.menu = [
            AvaiableCoffee(name="latte", water=200, milk=150, coffee=24, price=2.5),
            AvaiableCoffee(name="espresso", water=50, milk=0, coffee=18, price=1.5),
            AvaiableCoffee(name="cappuccino", water=250, milk=50, coffee=24, price=3),
        ]

    def presenting(self):
        m= ""
        for i in self.menu:
            m += f"{i.name}, {i.price} $ \n"
        return m

    def chooseCoffee(self, coffee):
        for i in self.menu:
            if i.name == coffee:
                return i
        print("No such coffee")

