start = float(input())
rente = float(input())
jaren = int(input())

#index voor jaar
j = 1
#bedrag is wat we uiteindelijk als output zullen hebben
bedrag = start

#j = 1 komt overeen met jaar 1, j = 2 komt overeen met jaar 2...
while j <= jaren:
    #'nieuwe' bedrag = bedrag * (1 + rente)
    bedrag *= (1 + rente)
    print(f"Bedrag na {j} jaar: €{bedrag:.2f}.")
    #ga naar volgende jaar
    j += 1

resultaat = bedrag - start
if resultaat > 0: #winst
    print(f"Na {jaren} jaar bedraagt de winst €{resultaat:.2f}.")
else: #verlies
    print(f"Na {jaren} jaar bedraagt het verlies €{abs(resultaat):.2f}.") #gebruik de absolute waarde voor een niet negatieve weergave van de output