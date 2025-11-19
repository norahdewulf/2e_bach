from loan import Loan

def main():
    # Enter yearly interest rate
    annualInterestRate = float(input("Enter yearly interest rate, for example, 7.25: "))

    # Enter number of years
    numberOfYears = int(input("Enter number of years as an integer: "))

    # Enter loan amount
    loanAmount = float(input("Enter loan amount, for example, 120000.95: "))

    # Enter a borrower
    borrower = input("Enter a borrower's name: ")

    # Create a Loan object
    loan1 = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)

    # Display loan date, monthly payment, and total payment
    print("The loan is for", loan1.getBorrower())
    print("The monthly payment is", format(loan1.getMonthlyPayment(), '.2f'))
    print("The total payment is", format(loan1.getTotalPayment(), '.2f'))

main() # Call the main function