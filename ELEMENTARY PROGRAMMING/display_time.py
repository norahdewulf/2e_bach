seconds = int(input("Enter the number of seconds: "))

#find minutes in seconds
#// is integer deling (geheel)
minutes = seconds // 60

#seconds remaining
remainingseconds = seconds % 60

print(seconds, "seconds is", minutes, "minutes and", remainingseconds, "seconds")