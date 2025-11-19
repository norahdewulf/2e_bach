gewicht = float(input())
lengte = float(input())

bmi = gewicht / (lengte ** 2)
print(bmi)

if bmi < 18:
    print("Ondergewicht")
elif 18 <= bmi < 25:
    print("Normaal gewicht")
elif 25 <= bmi < 30:
    print("Overgewicht")
else:
    print("Obesitas")