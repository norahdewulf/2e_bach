def main():
    x = 1
    print("Before the call, x is", x)
    #we gebruiken de increment functie die hieronder gedefinieerd wordt in de main functie
    #y = x
    increment(x) #increment is niet assigned aan iets (j = ...)
    print("After the call, x is", x)

def increment(y):
    y += 1
    print("\ty inside the function is", y)

main()