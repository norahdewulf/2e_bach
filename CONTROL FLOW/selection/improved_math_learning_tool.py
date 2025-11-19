import random

#OPTELLING
getal_1 = random.randint(1,20)
getal_2 = random.randint(1,20)

print("Geef de som van " + str(getal_1) + " en " + str(getal_2))
result = int(input())

#print(result)
#print(getal_1 + getal_2)

if result == getal_1 + getal_2:
    print("juist")
else:
    print("fout")

print(result == getal_1 + getal_2)

#VERSCHIL
getal_1 = random.randint(1,20)
getal_2 = random.randint(1,20)

#switch de 2 getallen als getal1 kleiner is anders berekent het verschil een negatief getal (wat we niet willen)
if getal_1 < getal_2:
    #old_getal1 = getal_1
    #getal_1 = getal_2
    #getal_2 = old_getal1
    getal_1, getal_2 = getal_2, getal_1

print("Geef het verschil tussen " + str(getal_1) + " en " + str(getal_2))
result = int(input())

#print(result)
#print(getal_1 + getal_2)

if result == getal_1 - getal_2:
    print("juist")
else:
    print("fout")

print(result == getal_1 - getal_2)