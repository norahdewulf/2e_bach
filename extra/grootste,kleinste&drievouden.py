x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())
x7 = int(input())
x8 = int(input())
x9 = int(input())
x10 = int(input())

getallen = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

maximum = max(getallen)
minimum = min(getallen)

aantal_drievouden = 0
for i in getallen:
    if i % 3 == 0:
        aantal_drievouden += 1

#andere manier: aantal_drievouden = sum(1 for i in getallen if i % 3 == 0)
#tel 1 op bij aantal_drievouden voor elke i die...

print(f"grootste: {maximum}")
print(f"kleinste: {minimum}")
print(f"drievouden: {aantal_drievouden}")