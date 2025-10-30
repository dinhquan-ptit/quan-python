a = float(input('Hãy nhập  điểm cuối năm của bạn = '))
if a > 10 :
    print('hãy nhập lại điểm của bạn dưới 10 điểm ')
    a = float(input('Hãy nhập lại điểm cuối năm của bạn = '))
if a >= 8 :
        print('bạn thuộc loại giỏi')
elif a >= 6.5 :
        print(' bạn thuộc loại khá ')
elif a >= 5 :
        print(' bạn thuộc loại trung bình ')
else :
        print(' bạn thuộc loại yếu')
