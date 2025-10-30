a = [ 1,2,3,4]
b = [ 5,9,7,8,6]
b.sort()
c = [*a,*b]
d = [x + y for x,y in zip(a,b)]
print(d)
print(c)