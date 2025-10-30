a = list(map(int,input('hãy nhập những số nguyên dương ( cách nhau bằng dấu cách) :').split()))
print(a)
c =[]
for i in a :
    if i not in  c :
        c.append(i)
print('danh sách sau khi bỏ trùng lặp là :',c)