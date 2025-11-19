def analyze_numbers(numbers: list):
    #eerst berkenen we het gemiddelde (van de list 'numbers')
    Gemiddelde = sum(numbers) / len(numbers)

    #dan vergelijken we alle elementen uit de lijst met dat gemiddelde
    #count staat vr de hoeveelheid getallen die boven het gemiddelde liggen
    count = 0
    #j is index voor de elementen die we aanduiden in de lijst (binnen de lengte van de lijst natuurlijk)
    for j in range(len(numbers)):
        if numbers[j] > Gemiddelde:
            count += 1
    print(f'Average is {Gemiddelde:.2f}')
    print(f'Number of elements above the average is {count}')

analyze_numbers([10, 15, 20, 25, 30])