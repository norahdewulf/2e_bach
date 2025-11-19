getal = int(input())

if getal % 2 == 0 and getal % 3 == 0:
    print("deelbaar door 2 en 3")
elif getal % 2 == 0 or getal % 3 == 0:
    print("deelbaar door 2 of 3")
elif getal % 2 == 0:
    print("deelbaar door 2, niet door 3")
else:
    print("deelbaar door 3, niet door 2")