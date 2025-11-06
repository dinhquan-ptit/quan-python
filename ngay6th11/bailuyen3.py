# bài toán đoán số 
import random
r = random.randint(1,100)
a = None
while a != r :
    a = int(input('hãy nhập số mà bạn cho là đúng từ 1 - 100 :  '))
    if a < r:
        print('số bạn nhập nhỏ hơn số cần đoán')
    elif a > r:
        print('số bạn nhập lớn hơn số cần đoán')
print('chúc mừng bạn đã đoán đúng số cần tìm')