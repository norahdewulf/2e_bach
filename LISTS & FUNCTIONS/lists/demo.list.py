def lin_search(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
    return -1

result = lin_search([1, 2, 3, 7, 8, 12], 3)
print(result)