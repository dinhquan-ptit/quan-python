lst = list(map(int, input("Nhập list số nguyên, cách nhau bởi khoảng trắng: ").split()))
a = []
for x in lst :
    if x > 10 and x %2 == 0 :
        a.append(x)
print(a)