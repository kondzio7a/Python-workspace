class CoffeeMaker(object):
    def __init__(self):
        self.resources = {
            "water": 1000,
            "coffee": 400,
            "milk": 500,
        }
    def report(self):
        print(f"Water available: {self.resources['water']} ml")
        print(f"Coffee available: {self.resources['coffee']} g")
        print(f"Milk available: {self.resources['milk']} ml")

    def check_resource(self, coffee):
        make_coffee = True
        for item in coffee.ingredients:
            if coffee.ingredients[item] > self.resources.get(item):
                print(f"Sorry, {item} is not available, please add")
                make_coffee = False
        return make_coffee
    
    def recources(self, coffee):
        for item in coffee.ingredients:
            self.resources[item] -= coffee.ingredients[item]
        return self.report()