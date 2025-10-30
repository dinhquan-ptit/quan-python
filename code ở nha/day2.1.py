ho_va_ten= '                đinh minh quân\n                '
a = 'Dinh'
b = '\nquân\n'

print(ho_va_ten*3)
print(ho_va_ten.title())
print(ho_va_ten.lower())
print(ho_va_ten.upper())
c = a +" "+ b
print(c)
d = 'xin chào '+ c.title()+ '!'
print(d)
print(ho_va_ten.rstrip())
print(ho_va_ten.lstrip())
print(ho_va_ten.strip())
print(ho_va_ten.capitalize())
print(b.center(50,'#'))
text = "This is a string."
print("Index of 'is' in text:", text.find("i"))
e = ['dinh','mih','quan']
f = "  ".join(e).upper()
print(f)