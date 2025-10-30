a = int(input(' số n = '))
b = 0
for a in range (0,a+1):
    if a % 2==0 :
        b += 1
print(f'có tất cả {b} số chẵn')