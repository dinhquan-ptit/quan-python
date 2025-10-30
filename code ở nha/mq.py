a = int(input('hãy nhập một số nguyên dương a :'))


sun= 0
for a in range(1,1+a):
    if a % 2 ==0:
        sun = sun + a
print(f'tổng các số từ 1 đến {a} là : ',sun)

