a = float(input('hãy nhập số kw bạn tiêu thụ :'))
while True:
    if a <0 :
        a = int(input('hãy nhập số kw bạn tiêu thụ :'))
    if a ==0 :
        print('bạn không tiêu thụ điện')
        break
    if a <= 50:
        b = a*1.800
    elif a <= 100:
        b = 50*1.800+(a-50)*2.000
    else :
        b = 50*1.800 + 50*2.000 + (a-100)*2.500
    print(f"số tiền cần nộp khi tiêu thụ {a}kw là:",b)
    break

        