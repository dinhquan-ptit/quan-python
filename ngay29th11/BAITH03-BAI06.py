k = ["apple", "banana", "orange", "mango", "grape", "kiwi", "pineapple", "watermelon"]
t = 0 
p = len(k)-1
while t < p :
    k[t],k[p]=k[p],k[t]
    t += 1 
    p -= 1 
print(k)

