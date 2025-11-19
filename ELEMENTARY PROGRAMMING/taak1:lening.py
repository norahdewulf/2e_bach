rente = float(input()) #in de formule nog delen door 100 om er een percentage van te maken
jaren = float(input())
bedrag = float(input())

maandrente = rente / 12

maandbetaling = (bedrag * maandrente / 100) / (1 - (1 / ((1 + maandrente / 100) ** (jaren * 12)))) #vergeet rente niet te delen door 100!
totaalbetaling = maandbetaling * 12 * jaren #vergeet niet te vermenigvuldigen met jaren

#cijfers achter de komma weglaten dus integer van maken!
print("The monthly payment is " + str(int(maandbetaling)))
print("The total payment is " + str(int(totaalbetaling)))