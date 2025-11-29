a = [1,2,3,4,5,6,5,5,7]
b = [4,5,6,7,8,9,10]
c = [x + y for x,y in zip(a,b)]
print(c)
d = [x - y for x,y in zip(a,b)]
print(d)
giao = []
print(giao)
for x in a:
    if x in b and x not in giao:
        giao.append(x)
print(giao)
