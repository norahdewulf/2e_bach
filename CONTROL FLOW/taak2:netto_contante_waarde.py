invest = float(input())
jaren = int(input())
rente = float(input())

#index voor jaar
j = 0 #mag niet j = 1 WANT in sommatie teken starten ze vanaf 0
npv = -invest #start met negatieve investering

while j < jaren:
    #verschillende inputs voor de verschillende jaren
    inkomst = float(input())
    uitgave = float(input())
    opbrengst_jaar = inkomst - uitgave
    npv += opbrengst_jaar / ((1 + rente) ** j)
    j += 1

print(f"De netto contante waarde over {jaren} jaar is €{npv:.2f}.")

if npv > 0:
    #je moet nog de winst berekenen
    winst = -invest + npv
    print(f"Hoera! Er wordt een winst geboekt van €{winst:.2f}!")
elif npv < 0:
    winst = -invest + npv
    print(f"Er is helaas een verlies van €{winst:.2f}.") #geen absolute waarde want in verliessituatie wordt de output als een negatief getal weergegeven
else:
    print(f"Er wordt exact break-even gedraaid.")