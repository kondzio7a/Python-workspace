import random
from game_data import data


random_a = random.choice(data)

def printing(x):
    name = x["name"]
    description = x["description"]
    country = x["country"]
    return f"{name}, a {description}, from {country}"


def check_value(value_a, value_b):
    if value_a > value_b:
        return "a"
    else:
        return "b"

game_continue = True
score = 0
while game_continue:
    print(f"\n\nYour score is: {score}")
    random_b = random.choice(data)

    while random_b == random_a:
        random_b = random.choice(data)

    print(f"{printing(random_a)}\n         VS \n{printing(random_b)}")
    count_a = int(random_a["follower_count"])
    count_b = int(random_b["follower_count"])

    value_player = input("\nWho has more followers? A or B: ").lower()
    while value_player not in ("a", "b"):
        value_player = input("\nWho has more followers? A or B: ").lower()

    right_answer = check_value(count_a, count_b)

    if right_answer == value_player:
        if right_answer == "a":
            score += 1
        else:
            random_a = random_b
            score +=1
    else:
        print(f"Wrong Answer, You lose.Your score is {score}"
              f""
              f""
              f""
              f"")
        game_continue = False











