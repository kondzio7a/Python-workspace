def format_name():
    f_name = input("Please enter your first name: ").title()
    l_name = input("Please enter your last name: ").title()
    return f"{f_name}  {l_name}"

format_name = format_name()
print(format_name)