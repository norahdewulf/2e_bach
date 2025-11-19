total = float(input("Enter the total amount:"))
tip = float(input("Enter the tip percentage you wish to give:"))

tip_percentage = tip / 100
amount = total + (total * tip_percentage)
amount_rounded = int(amount * 100) / 100 #vergeet niet de int toe te voegen om het getal te tonen op 2 decimalen na komma (niet gelijk aan afronden)

print("Total amount including tip: " + str(amount_rounded))