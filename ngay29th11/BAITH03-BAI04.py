ds = ["apple", "banana", "orange", "apple", "kiwi", "apple"]
while True :
    a = input('nhập từ cần tra ')
    if a in ds :
        print('từ có trong danh sách ')
    else :
        print('từ không có trong danh sách :')
    k = input('nhập c để tiếp tục tra')
    if k != 'c':
        break
