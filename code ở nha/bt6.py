S = input("Nhập vào một chuỗi: ")

digits = []
for ch in S:
    if ch.isdigit():
        digits.append(int(ch))

if digits:
    print("Các chữ số xuất hiện trong chuỗi là:", digits)
    print("Tổng các chữ số là:", sum(digits))
else:
    print("Thôi nào, tôi mệt quá.!")
