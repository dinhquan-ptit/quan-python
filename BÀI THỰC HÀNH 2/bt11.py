a = list(map(int,input('hãy nhập các số nguyên dương và cách nhau bằng đấu cách :').split()))
sum = 0
for i in a :
    if i % 2 == 0 :
        sum += i 
print(sum)