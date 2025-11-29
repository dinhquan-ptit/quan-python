lst = [1, 2, 2, 3, 3, 3, 4]
b = {}
for i in lst :
    if i in b :
        b[i] += 1 
    else :
        b[i] = 1
print(b)