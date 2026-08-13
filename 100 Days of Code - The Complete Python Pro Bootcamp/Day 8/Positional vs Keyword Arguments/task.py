def is_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False



x = int(input("Wpisz date"))
print(is_leap_year(x))