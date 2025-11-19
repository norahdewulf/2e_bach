nested_list = eval(input())
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)