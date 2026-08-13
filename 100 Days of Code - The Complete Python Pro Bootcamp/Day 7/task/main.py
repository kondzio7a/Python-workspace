import random
word_list = ["aardvark", "baboon", "camel"]
blank = "_"
placeholder = blank * len(word_list)
correct = []

choise = random.choice(word_list)
print(choise)

while placeholder != choise:
    guess = input("Enter a letter: ")
    placeholder = ""
    for letter in choise:
        if letter == guess:
            placeholder += letter
            correct.append(letter)
        elif letter in correct:
            placeholder += letter
        else:
            placeholder += blank
    print(placeholder)
