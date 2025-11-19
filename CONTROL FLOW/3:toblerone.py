merk = input("Enter your brand: ")
stad = input("Enter your city: ")
lengte_merk = len(merk)
lengte_stad = len(stad)

#in het begin is onze "output" (ons uiteindelijk resultaat) nog leeg want we vullen deze aan tijdens de oefening
output = ""
i = 0  # Index voor merk
j = 0  # Index voor stad

#STAP 1
#merknaam overlopen van links nr rechts: check letter in merk =? in stad => volgende letter checken in merk =? stad... totdat alle letters zijn gecheckt in stad en of deze overeenkomen met de letter die we 'vast hebben' van merk
#outer loop: zolang onze index de lengte van onze merknaam niet overschrijdt voeren we deze uit
while i < lengte_merk:
    if j < lengte_stad and merk[i].lower() == stad[j].lower():
        #we vullen onze output aan
        output += "[" + merk[i] + "]"
        #we verhogen onze j & i
        j += 1
        i += 1
    else:
        output += merk[i]
        i += 1 #geen j += 1 WANT hij zou beginnen zoeken bij volgende karakter van stad ookal is de vorige n gevonden in merk

#STAP 2
#afwerking
output = output.replace("][", "")

#ook een mogelijkheid maar ingewikkeld:
#while "][" in output:
    #k = output.index("][")              # Index voor "][" in result => maak er een variabele k van
    #output = output[:k] + output[k+2:]  # Nieuwe string van [start, k[ + [k+2, eind], dus minus "][" => we skippen "][" => eerste index: k zit n meer in interval MAAR k-1 wel nog

print(output)