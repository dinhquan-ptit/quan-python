tu_dien = {'name':'tên','hello':'xin chào','what':'cái gì'}
while True :
    # hiện thị menu 
    print('-----TỪ ĐIỂN ANH VIỆT-----')
    print('1- tra từ điển ')
    print('2- thêm từ điển ')
    print('3- xóa từ điển ')
    print('4- thoát chương trình ')
    a = input('bạn hãy chọn chứ năng từ 1-4\n')
    #----------
    # chức năng 1 
    #----------
    if a == '1':
        while True:
            tu = input('\n nhập từ tiếng anh cần tra hoặc chọn 0 để quay lại ')
            if tu == '0':
                break
            if tu in tu_dien :
                print(f'từ {tu} có nghĩa là : {tu_dien[tu]}')
            else :
                print(f'từ {tu} khoong thuộc trong từ điển anh việt ')
            tiep = input('bạn có muốn tra từ điển nữa không (y/n)').lower()
            if tiep != 'y' :
                break
    #----------
    # chức năng 2
    #----------
    elif a == '2':
        while True :
            b = input('nhập từ tiếng anh cần thêm hoặc chọn 0 để quay lại ')
            if b == '0 ':
                break
            if b in tu_dien :
                print('từ đã có trong từ điển rồi ')
            else:
                gtr = input('hãy nhập nghĩa của từ điển trên ')
                tu_dien[b]= gtr
                print('đã thêm từ điển thành công ')

            tiep = input('bạn có muốn tra từ điển nữa không (y/n)').lower()
            if tiep != 'y' :
                break
    #-------
    # chức năng 3
    #-------
    elif a == '3':
        while True :
            c = input('hãy nhập từ mà bạn muốn xóa hoặc nhấn 0 để quay lại ')
            if c == '0':
                break
            if c not in tu_dien :
                print('từ này không có ở trong từ điển ')
            else :
                del tu_dien[c]
                print('từ điển đã được xóa ')
                print(tu_dien)
            d = input('bạn có muốn xóa tiếp không (y/n)')

            if d != 'y' :
                break 
    #------
    # chức năng 4 
    #------
    elif a == '4':
        print ('cảm ơn bạn đã sử dụng ')
        print('chúc bạn một ngày tốt lành ')
    else :
        print('bạn đã ghi sai cú pháp hãy chọn lại')