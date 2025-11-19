def display_average_hours(weekly_hours_table: list):
    #index voor de lijst
    k = 0
    gemiddelde = []

    while k < len(weekly_hours_table):
        #voeg wat er op de kde index staat toe aan onze gemiddelde lijst op de k+1de index
        gemiddelde.append((sum(weekly_hours_table[k])) / len (weekly_hours_table[k]), k + 1)
        k += 1

    aantaluren = sorted(gemiddelde, reverse=True)

    print("Employee, Average Daily Hours")
    print("---------------------------------")

    for a, b in aantaluren:  # Elke tuple in werkuren bevat (gemiddelde, werknemer_id)
        print(f"Employee {b}	{a:.2f} hours")

#zie een matrix als een lijst van lijsten [[1,2], [5,6], [8,9]]