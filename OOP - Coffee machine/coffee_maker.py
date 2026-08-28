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

    def check_resource(self, coffee):
        make_coffee = True
        for item in coffee.ingredients:
            if coffee.ingredients[item] > self.resources.get(item):
                print(f"Sorry, {item} is not available, please add")
                make_coffee = False
        return make_coffee