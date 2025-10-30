a = input('hãy nhập danh sách các chữ :').split()
print('chuỗi trên có độ dài là ', len(a))
b = {}
for i in a :
    if i in b :
        b[i]+=1
    else :
        b[i] = 1
print(b)

