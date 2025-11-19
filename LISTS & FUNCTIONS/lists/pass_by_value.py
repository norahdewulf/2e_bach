def main():
    x = 1 # x represents an int value => immutable
    y = [1, 2, 3] # y represents a list => changeable
    m(x, y) # Invoke f with arguments x and y
    print("x is " + str(x)) # => output: 1 (because immutable)
    print("y[0] is " + str(y[0])) # => output: 5555 (because changeable)

def m(number, numbers):
    number = 1001 # Assign a new value to number
    numbers[0] = 5555 # Assign a new value to numbers[0]

main()