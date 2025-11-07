# cách sử dụng def trong python
#def chao():
    #print('chào mừng bạn đến với python ')
#chao()
#def tinh_tong(a,b):
    #return a+b
#kq = tinh_tong(5,7)
#print('tổng hai số là :',kq)
def tong(*s):
    return sum(s)
print('tổng các số là :',tong(1,2,3,4,5))
#def binh_phuong(a):
#    return a ** 2
#for i in range (1,6):
#    print(f'bình phương của {i} là : {binh_phuong(i)}')


# bài toán số chẵn lẻ sử dụng def

def chan_le (a):
    if a % 2 ==0 :
        return 'số chẵn'
    else :
        return 'số lẻ'
k = int(input('hãy nhập một số nguyên dương :'))
print(f'số {k} là : {chan_le(k)}')
def giai_thua(a):
    gt = 1
    for i in range (1,a+1):
        gt *=i
    return gt
m = int(input('hãy nhập một số nguyên dương :'))
print(f'giai thừa của số {m} là : {giai_thua(m)}')
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def dem_nguyen_to(ds):
    dem = 0
    for so in ds:
        if la_so_nguyen_to(so):
            dem += 1
    return dem

print(dem_nguyen_to([2, 3, 4, 5, 10, 11]))
