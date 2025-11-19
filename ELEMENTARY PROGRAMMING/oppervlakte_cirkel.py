straal_txt = input("Geef een waarde voor de straal?")
straal = int(straal_txt)
#korter: straal = int(input("Geef een waarde voor de straal?"))
PI = 3.141592653589793

opp = PI * straal * straal

#komma -> programma voegt in oplossing automatisch een spatie toe: "... is 28.27..."
print("De opp van de cirkel is", opp)
#andere manier -> n automatisch een spatie
print("De opp van de cirkel is "+ str(opp))