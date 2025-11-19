#in deze oefening hebben we een grote outer loop => de loop blijft uitgevoerd worden tot de gebruiker het programma wenst af te sluiten
#noodzakelijk omdat je op het einde van je loop een break hebt zitten, break = false => while loop stopt
#ook de inputs zitten binnenin de loop want voor elke keer dat het programma uitgevoerd wordt hebben we nieuwe inputs
while True:
    werknemers = int(input())
    jaaromzet = float(input())
    balanstotaal = float(input())
    percentage = int(input())

    #vergeet niet OR tussen jaaromzet en balanstotaal want AND is fout (zie opgave tabelletje)
    if (werknemers < 250) and (jaaromzet < 50000 or balanstotaal < 43000) and (percentage <= 25):
        print("Het bedrijf is EEN KMO")
    else:
        print("Het bedrijf is GEEN KMO")

    #de gebruiker beslist of hij het programma nog eens wil laten uitvoeren (ja) of wilt stoppen (nee) (hoofdletter ongevoelig!)
    vervolg = input().lower()
    if vervolg != "ja":
        break