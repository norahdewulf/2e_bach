def check_palindrome(input):
    string = input.replace(" ", "").lower() #maak de input niet-hoofdlettergevoelig en verwijder spatie(s)
    if string == string[::-1]: #de string wordt gereversed
        print(f"The string {input} is a palindrome.")
    else:
        print(f"The string {input} is not a palindrome.")

check_palindrome("Hannah")
check_palindrome("Ugent")