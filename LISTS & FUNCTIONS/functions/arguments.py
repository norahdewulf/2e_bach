def nPrintln(message, n):
    for i in range (0, n):
        print(message)

#2 verschillende manieren om een functie op te roepen
#1. by position
#nPrintln(“Welcome to Python”, 5) => correct
#nPrintln(4, “Computer Science”) => NIET correct

#2. keywords arguments
#nPrintln(n = 4, message = "hello") => correct