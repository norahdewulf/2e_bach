print("Multiplication Table")

for i in range(1, 10): #deze range gaat niet tot 10! maar gaat wel tot 9 (dus getal 1 tem 9 uitgeprint)
    print(i, end=" ") #ipv van ze onder elkaar te printen worden ze naast elkaar geprint

print() #zorgt ervoor dat de streepjes op de volgende lijn komen te staan
print("---------------------------")

for j in range(1, 10):
    print(j, "|", end=" ") #alle getallen worden naast elkaar geprint
    for k in range(1, 10):
        print(k*j, end=" ")
    print() #zorgt ervoor dat voor de volgende j van de for-loop de getallen op de volgende lijn komen te staan