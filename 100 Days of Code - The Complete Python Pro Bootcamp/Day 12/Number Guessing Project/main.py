import random
choice = ""
random_number = random.randint(1, 100)
print(random_number)

def difficult(x):
    for i in range(x,0,-1):
        print(f"You have {i} attempts remaining to guess the number.")
        number = int(input("Make a guess: "))
        if number == random_number:
            print("Congratulation you win")
            return
        elif number > random_number:
            print(f"Sorry {number} is too high")
        else:
            print(f"Sorry {number} is too low")
    print("You lose because attempts are finished")


print("I'm thinking of a number between 1 and 100")
while choice not in ["easy", "hard"]:
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == "easy":
        difficult(10)
    elif choice == "hard":
        difficult(5)
    else:
        print("Sorry, wrong choose we haven t that option")