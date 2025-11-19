getal = int(input())

#filter degene die al zeker geen priemgetal zijn (kleiner dan 2) weg
if getal < 2:
    print(f"{getal} is geen priemgetal")
else:
    for i in range(2, int(getal ** 0.5) + 1): #range begint vanaf getal 2 EN einde is grootst mogelijke deler v getal (wortel + 1)
        if getal % i == 0: #dit wil zeggen dat het getal meer gehele delers heeft dan zichzelf
            print(f"{getal} is geen priemgetal")
            break #vermijden dat hij het zinnetje "... is geen priemgetal" niet 2 keer print (resultaat van de for loop wordt geskipt => springt uit for loop)
        else:
            print(f"{getal} is een priemgetal")