a = ' tôi tên là đinh minh quân ,  tôi đang học lớp udu25'
c = a.strip().split()
d = " ".join(c)
print(d)
b = d.capitalize()
print(b)
if not b.endswith(' .'):
    b += ' .'
    print(b)

