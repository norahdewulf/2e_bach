#1 is de kleinst mogelijke echte deler

def som_delers(n):
    list = []
    #voor alle getallen v 1 tot n (zichzelf is g echte deler! => n niet meer in range)
    for i in range(1, n):
        #zoek naar de echt delers van n en voeg ze toe aan de empty list
        if n % i == 0:
            list.append(i)

    #bereken de som van alle echte delers
    b = sum(list)
    return b

def getalsoort(n):
    #som_delers(n) = b
    if som_delers(n) == n:
        return "perfect"
    elif som_delers(n) < n:
        return "gebrekkig"
    else:
        return "overvloedig"

print(som_delers(28))
print(getalsoort(28))
print(getalsoort(29))