alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(orginal_text, shift_amount):
    t = ""
    for letter in orginal_text:
        id= alphabet.index(letter)
        id = (id + shift_amount) % 26
        t += alphabet[id]
    print(t)

def decrypt(orginal_text, shift_amount):
    t = ""
    for letter in orginal_text:
        id= alphabet.index(letter)
        id = (id - shift_amount) % 26
        t += alphabet[id]
    print(t)

