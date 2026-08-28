class CoffeeMaker(object):
    def __init__(self):
        self.resources = {
            "water": 1000,
            "coffee": 400,
            "milk": 500,
        }
    def report(self):
        print(f"Capacity of water {self.resources.get('water')}")
        print(f"Capacity of coffee {self.resources.get('coffee')}")
        print(f"Capacity of milk{self.resources.get('milk')}")

    