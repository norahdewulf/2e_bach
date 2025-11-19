import random

aantal_oef = int(input("Aantal oefeningen ?"))
#index voor aantal oefeningen
i = 0

while i < aantal_oef:
    getal_1 = random.randint(1,20)
    getal_2 = random.randint(1,20)

    #zodat het verschil tussen de 2 niet negatief ingevoerd moet worden
    if getal_1 < getal_2:
        getal_1, getal_2 = getal_2, getal_1

    print("Geef het verschil tussen " + str(getal_1) + " en " + str(getal_2))
    result = int(input())

    while result != getal_1 - getal_2:
        print("Fout antwoord")
        print("Geef het verschil tussen " + str(getal_1) + " en " + str(getal_2))
        #geef opnieuw een antwoord in
        result = int(input())
        #while loop blijft doorgaan totdat het resultaat correct is

    #while loop stopt want FALSE
    print("Juist antwoord")
    #ga naar de volgende oefening
    i += 1

#buiten while loop stopt als het gewenste aantal oefeningen uitgevoerd zijn