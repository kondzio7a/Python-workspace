import menu as m
menu = m.Menu()
print(menu.presenting())

choice_coffee = input("What would you like to drink? ").lower()
print(menu.chooseCoffee(choice_coffee))