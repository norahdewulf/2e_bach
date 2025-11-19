def main():
    #deze inputs staan binnen de functie want het is een main() functie, bij een gewone functie is dit uiteraard niet zo
    gewicht = float(input())
    lengte_cm = int(input()) #lengte in centimeter

    #lengte omzetten nr meter
    lengte = lengte_cm / 100

    bmi = gewicht / (lengte ** 2)
    print(f"{bmi:.2f}")

    if bmi < 18:
        print("Ondergewicht")
    elif 18 <= bmi < 25:
        print("Normaal gewicht")
    elif 25 <= bmi < 30:
        print("Overgewicht")
    else:
        print("Obesitas")

main()

#test lokaal
#if __name__ == "__main__":
    #main()