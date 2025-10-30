a = list(map(int,input('hãy nhập các số : ').split()))
b = None
c = 0 
for i in a :
    if a.count(i) > b :
        b = a.count(i)
        c = i
print('giá trị xuất hiện nhiều nhất là  :', i )
print('số lần xuất hiện của giá trị la :', b)
