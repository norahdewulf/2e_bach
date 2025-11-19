def gemeenschappelijke_karakters(s1, s2):
    lengte_s1 = len(s1)
    lengte_s2 = len(s2)
    i = 0 #index vr s1
    gk = []

    while i < lengte_s1:
        j = 0 # Reset j for each new character in s1 (we willen elke letter dat we vast hebben van s1 vergelijken met alle letters van s2)
        while j < lengte_s2:
            if s1[i].lower() == s2[j].lower():
                if s1[i].lower() not in gk:
                    gk.append(s1[i].lower())
            #we gaan naar de volgende letter van s2 en vergelijken de letter die we vast hebben van s1 ermee
            j += 1

        #als we de letter van s1 (i) die we 'vast hebben' vergeleken hebben met alle letters in s2 (alle j), dan gaan we naar de volgende i in s1 en vergelijken we die met alle letters in s2
        i += 1

    return len(gk)

print(gemeenschappelijke_karakters("een", "twee"))