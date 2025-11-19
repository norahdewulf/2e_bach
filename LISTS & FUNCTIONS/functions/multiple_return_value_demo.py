def sort(number1, number2):
    if number1 < number2:
        return number1, number2
    else:
        return number2, number1

#n1 en n2 worden gedefinieerd met behulp van de functie
n1, n2 = sort(3, 2)
#wat deze functie returnt: (2, 3)
print("n1 is", n1)
print("n2 is", n2)