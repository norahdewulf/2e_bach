s= "Welcome"
print(s[1], end=" ")
print(s[-1], end=" ")
print(s[-1+len(s)], end=" ")
print(s[4:],end=" ")
print(s[1: -1+len(s)])

n = 20000.989
print(round(n, 2))
print(f"{n:.2f}")