import random

getal = random.randint(1, 100)

gok = int(input("Guess a number between 1 and 100: "))

while gok != getal: #zolang deze statement TRUE is zal de while loop uitgevoerd worden
    if gok > getal:
        print("Too high")
    else:
        print("Too low")
    #vraag naar een nieuwe gok
    gok = int(input("Guess a number again: "))
    #de while loop blijft doorlopen tot de gok juist is

print("Thank you for playing!")