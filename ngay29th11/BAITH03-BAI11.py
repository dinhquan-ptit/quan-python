dict1 = {'a': 2, 'b': 3, 'c': 1}
dict2 = {'b': 4, 'c': 5, 'd': 6}
for key, value in dict2.items():
    if key in dict1:
        dict1[key] += value
    else:
        dict1[key] = value
print(dict1)
