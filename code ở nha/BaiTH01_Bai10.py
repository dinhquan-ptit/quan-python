a = int(input('hãy nhập năm bạn cần xem :'))
if a % 4 == 0 and a % 100 != 0 :
    print(f' năm {a} là năm nhuận ')
else :
    print(f' năm {a} là năm không nhuận')