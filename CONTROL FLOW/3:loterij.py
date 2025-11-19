import random

nummer = int(input("Enter your lottery pick (two digits):"))

random.seed(1)
loterij = random.randint(0, 99)
print("The lottery number is " + str(loterij))

if nummer == loterij:
    print("Exact match: you win 10.000 €")
#bij de volgende stap sorteren we alle nummers (die worden omgezet nr strings) en als deze gelijk zijn wil dit zeggen dat de nummers dezelfde getallen bevatten maar bv een andere initiele volgorde hebben maar dit wil nogsteeds zeggen dat de getallen overeenkomen
elif sorted(str(nummer)) == sorted(str(loterij)):
    print("Match all digits: you win 3.000 €")
#any() returns een TRUE / FALSE, kijken of een nummer overeenkomt met een nummer in ander getal
elif any(digit in str(nummer) for digit in str(loterij)):
    print("Match one digit: you win 1,000 €")
else:
    print("Sorry, no match")

#goed bekijken