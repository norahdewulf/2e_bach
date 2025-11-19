#hoofdstring
zin = input("Geef de zin die het toverwoord bevat.")

#we zoeken 3 dingen: naam, toverwoord & lengte v toverwoord

#NAAM
#we zoeken naar de 'onveranderde' woorden in de basisstructuur van de zin
#we zoeken dus substrings
iss = zin.find("is")
enn = zin.find("en")
#begin te tellen vanaf "i" van "is"
#stop met tellen een digit voor en (wordt n meegenomen)
naam = zin[iss + 3 : enn - 1]

#TOVERWOORD
aanhalingstekens1 = zin.find('"')
#rfind zoekt naar de verste die gevonden kan worden id zin
aanhalingstekens2 = zin.rfind('"')
toverwoord = zin[aanhalingstekens1 : aanhalingstekens2 + 1] # niks bij 1 en +1 bij 2 want je wilt de aanhalingstekens meepakken

#LENGTE TOVERWOORD
lengte = len(toverwoord) - 2 #je wilt de aanhalingstekens niet meetellen

print(f"Het toverwoord van {naam} is {toverwoord}. De lengte van het toverwoord is {lengte} letters.")