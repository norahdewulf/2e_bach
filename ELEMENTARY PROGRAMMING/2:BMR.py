massa = int(input())
lengte = int(input())
leeftijd = int(input())

BMR_man = 66.4730 + (13.7516 * massa) + (5.0033 * lengte) - (6.7550 * leeftijd)
BMR_vrouw = 655.0955 + (9.5634 * massa) + (1.8496 * lengte) - (4.6756 * leeftijd)

print("Een man moet dagelijks " + str(BMR_man/ 230) + " chocoladerepen eten om zijn gewicht te behouden.")
print("Een vrouw moet dagelijks " + str(BMR_vrouw/ 230) + " chocoladerepen eten om haar gewicht te behouden.")