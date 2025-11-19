print("Ik vind voor jou de combinatie aan centjes dat overeenkomt met een bepaald bedrag.")
bedrag = int(input("Geef een bedrag tussen 0 en 100:"))

print(str(bedrag) + " centje(s) bestaat uit:")

bedrag1 = bedrag // 50
print(str(bedrag1) + " centje(s) van 50 cent")
bedrag2 = bedrag - (bedrag1 * 50)

bedrag3 = bedrag2 // 20
print(str(bedrag3) + " centje(s) van 20 cent")
bedrag4 = bedrag2 - (bedrag3 * 20)

bedrag5 = bedrag4 // 10
print(str(bedrag5) + " centje(s) van 10 cent")
bedrag6 = bedrag4 - (bedrag5 * 10)

bedrag7 = bedrag6 // 5
print(str(bedrag7) + " centje(s) van 5 cent")
bedrag8 = bedrag6 - (bedrag7 * 5)

bedrag9 = bedrag8 // 2
print(str(bedrag9) + " centje(s) van 2 cent")
bedrag10 = bedrag8 - (bedrag9 * 2)

bedrag11 = bedrag10 // 1
print(str(bedrag11) + " centje(s)")