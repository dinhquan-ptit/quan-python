
b = 20
while True:
    a = int(input('hãy nhập số n ( từ 0-50) :'))
    if a > b :
        print(f'số bí mật bé hơn {a}')
    elif a < b : 
        print(f'số bí mật lớn hơn {a}')
    else :
        print('bạn đã đoán đúng')
        break