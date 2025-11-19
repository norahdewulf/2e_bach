bloon = int(input("brutoloon werknemer:"))

rsz = bloon * -0.1307
belastb = bloon + rsz #optelling want rsz is een negatief getal
bedrijfvoor = belastb * -0.3
nettoloon = belastb + bedrijfvoor #optelling

print("=" * 42)
print(f"|{'LOONFICHE':^40}|") #^ centreren in de overblijvende 40 plaatsjes tussen de 2 streepjes (daarom niet 42)
print("=" * 42)
print(f"|{'Brutoloon':<28}|{bloon:>10.2f} |") #zet in het vakje van 28 plaatsjes 'burtoloon' volledig rechts EN zet bloon in een vak van 10 plaatjes volledig links + rond af
print(f"|{'-' * 40}|")
print(f"|{'RSZ bijdrage':<28}|{rsz:>10.2f} |")
print(f"|{'-' * 40}|")
print(f"|{'Belastbaar inkomen':<28}|{belastb:>10.2f} |")
print(f"|{'-' * 40}|")
print(f"|{'Bedrijfsvoorheffing':<28}|{bedrijfvoor:>10.2f} |")
print(f"|{'-' * 40}|")
print(f"|{'Nettoloon':<28}|{nettoloon:>10.2f} |")
print(f"|{'-' * 40}|")