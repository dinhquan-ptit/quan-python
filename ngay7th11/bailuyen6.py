#chương trình menu sử dụng nhiều hàm def 
def menu() :
    print('--------------------------------')
    print('------------MENU-----------')
    print('--------------------------------')
    print('1. tính tổng ')
    print('2. tính giai thừa ')
    print('3. kiểm tra số nguyên tố ')
    print('4. kiểm tra chẵn lẻ')
    print('5. thoát')
while True :
    menu()
    a = int(input('Chọn chức năng: '))
    if a == 1 :
        def tinh_tong ():
            n = int(input('hãy nhập số n '))
            sum = 0
            for i in range(1,n+1):
                sum += i
            print('Tổng từ 1 đến', n, 'là:', sum)
        tinh_tong()
    elif a == 2 :
        def giai_thua():
            n = int(input('hãy nhập số n '))
            giai_thua = 1
            for i in range (1,n+1):
                giai_thua *= i
            print('Giai thừa của', n, 'là:', giai_thua)
        giai_thua()
    elif a == 3 :
        def snt():
            n=int(input('hãy nhập số n '))
            if n <2 :
                print(n,'không phải là số nguyên tố')
            else :
                for i in range (2,int(n**0.5)+1):
                    if n % i == 0 :
                        print(n,'không phải là số nguyên tố')
                        break
                else :
                    print(n,'là số nguyên tố')
        snt()
    elif a == 4 :
        def chan_le():
            n = int(input('hãy nhập số n '))
            if n % 2 == 0 :
                print(n,'là số chẵn')
            else :
                print(n,'là số lẻ')
        chan_le()
    elif a == 5 :
        print('bạn đã thoát chương trình')
        break
    else :
        print('bạn đã nhập sai chức năng, vui lòng chọn lại')