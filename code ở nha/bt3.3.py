a = "quân"
b = ['anh','em ','tôi','bạn']
c = ['đông','thu']
e =[1,2,3]
f=[4,5,6]

b.append(a)
print(b)
b.extend(c)
print(b)
b.insert(2,a)
print(b)
d = e+f
print(d)
g= [element for list in [e, f] for element in list]
print(g)
import itertools
k = list(itertools.chain(e, f))
print(k)
q =[*e,*f]
print(q)
e += f
print(e)
del b[1]
b.pop(2)
