import pandas as pd
import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = {"A":11,"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
df = pd.DataFrame(cards.items(), columns=["Karty","Wartości"])
list_gracz = []
list_krupier = []
i = 0
suma = 0
decidion = ""
"""Karty gracza:"""
while i < 2:
    karta = random.choice(df["Karty"].values)
    wartosc_gracza = df.loc[df["Karty"] == karta, "Wartości"].values[0]
    list_gracz.append(karta)
    suma = suma + wartosc_gracza
    i = i + 1

karta_krupiera =  random.choice(df["Karty"].values)
wartosc_krupiera = df.loc[df["Karty"] == karta_krupiera, "Wartości"].values[0]
list_krupier.append(karta_krupiera)
suma_krupiera = wartosc_krupiera
print(f"Karty krupiera",list_krupier)
print(f"Karty gracza",list_gracz)
while suma <= 21 and decidion != "pass":
    decidion = input("Pass or draw: ").lower()

    if decidion == "draw":
        karta = random.choice(df["Karty"].values)
        wartosc_gracza = df.loc[df["Karty"] == karta, "Wartości"].values[0]
        list_gracz.append(karta)
        suma += wartosc_gracza
        print(f"Karty gracza",list_gracz)

    elif decidion == "pass":
        print(f"Karty gracza",list_gracz)
        print("Suma z kart:", suma)

    else:
        print("Invalid input")

if suma > 21:
    print(f"Suma z kart:", suma)
    print("Przegrałeś")
elif suma <= 21:
    while suma_krupiera <= 21 and suma > suma_krupiera:
        karta_krupiera = random.choice(df["Karty"].values)
        wartosc_krupiera = df.loc[df["Karty"] == karta_krupiera, "Wartości"].values[0]
        list_krupier.append(karta_krupiera)
        suma_krupiera += wartosc_krupiera

    print(f"Karty krupiera", list_krupier)
    if suma_krupiera > 21 :
        print(f"Wygrałeś krupier score: ", suma_krupiera," Twój score: ", suma)
    elif suma_krupiera <= 21 and suma > suma_krupiera:
        print(f"Wygrałeś krupier score: ", suma_krupiera, " Twój score: ", suma)
    elif suma_krupiera <= 21 and suma == suma_krupiera:
        print(f"Remis krupier score: ", suma_krupiera, " Twój score: ", suma)
    else:
        print(f"Przegrałeś krupier score: ", suma_krupiera, " Twój score: ", suma)



