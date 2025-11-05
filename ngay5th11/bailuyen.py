# bài toán về quản lý sản phẩm trong cửa hàng
sp = {'001': {'tên': 'Áo thun', 'giá': 150000, 'số lượng': 50,}
        , '002': {'tên': 'Quần jeans', 'giá': 300000, 'số lượng': 30,}
        , '003': {'tên': 'Giày thể thao', 'giá': 500000, 'số lượng': 20,}
        , '004': {'tên': 'Mũ lưỡi trai', 'giá': 100000, 'số lượng': 100,}
        }
while True:
    print('''Quản lý sản phẩm trong cửa hàng
    1. thêm sản phẩm mới 
    2. xóa sản phẩm 
    3. Cập nhật giá sản phẩm
    4. tính tổng tiền tồn kho ''')
    choice = input('hãy nhập lựa chọn của bạn (1-4) hoặc nhấn q để thoát : ')
    if choice == '1':
        ma_sp = input('hãy nhập mã sản phẩm : ')
        if ma_sp in sp:
            print(' sản phẩm đã tồn tại !')
        else:
            ten = input('hãy nhập tên sản phẩm : ')
            gia = int(input('hãy nhập giá sản phẩm : '))
            so_luong = int(input('hãy nhập số lượng sản phẩm : '))
            sp[ma_sp] = {'tên': ten, 'giá': gia, 'số lượng': so_luong}
            print(sp)
            print('thêm sản phẩm thành công !')
    
    elif choice == '2':
        ma_sp = input('hãy nhập mã sản phẩm muốn xóa : ')
        if ma_sp in sp:
            del sp[ma_sp]
            print('xóa sản phẩm thành công !')
        else:
            print('sản phẩm không tồn tại !')
    elif choice == '3':
        ma_sp = input('hãy nhập tên sản phẩm muốn cập nhật giá : ')
        if ma_sp in sp:
            gia_moi = int(input('hãy nhập giá mới cho sản phẩm : '))
            sp[ma_sp]['giá'] = gia_moi
            print('cập nhật giá sản phẩm thành công !')
        else:
            print('sản phẩm không tồn tại !')
    elif choice == '4':
        tong_tien = 0
        for chi_tiet in sp.values():
            tong_tien += chi_tiet['giá'] * chi_tiet['số lượng']
        print(f'tổng tiền tồn kho là : {tong_tien} VND')
    elif choice.lower() == 'q':
        print('thoát chương trình quản lý sản phẩm !')
        break
    else:
        print('lựa chọn không hợp lệ, vui lòng thử lại !')