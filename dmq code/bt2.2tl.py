a = [5,10,15,45,30,44]
a[1:3] =[4,7] 
print(a)
for i in range(len(a)):
    a[i] +=2
print(a)
a = [x +2 for x in a]
print(a)
a = list(map(lambda x: x+2, a))
print(a)
for i,x in enumerate(a):
    a[i]= x+2
print(a)
a = list(filter(lambda x: x%2==0 ,a))
print(a)
from functools import reduce
b = reduce(lambda x,y : x +y ,a)
print(b)