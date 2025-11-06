# công việc cần làm trong một ngày
cong_viec = [{'ten' : 'thức dậy','gio' : 6},
               {'ten' : 'đi học','gio' : 7},
               {'ten' : 'ăn trưa','gio' : 12},
               {'ten' : 'ngủ trưa','gio' : 13},
               {'ten' : 'học bài','gio' : 14},
               {'ten' : 'đi ngủ','gio' : 22},
                ]
print('công việc trong một ngày là :')
for cv in cong_viec:
    print(f" - {cv['ten']} vào lúc {cv['gio']} giờ")
while True:
    print('''MENU CÔNG VIỆC:
        1. Thêm công việc
        2. Xoá công việc
        3. Hiển thị công việc
        4. THAY ĐỔI GIỜ CÔNG VIỆC
        5. Thoát''')

    chon = input('hãy chọn công việc bạn muốn làm (1-5): ')
    if chon == '1':
            ten_cv = input('hãy nhập tên công việc bạn muốn thêm: ')
            while True:
                gio_cv = int(input('hãy nhập giờ cho công việc đó (0-23): '))
                if 0 <= gio_cv <= 23:
                    break
                else:
                    print('giờ không hợp lệ, vui lòng nhập lại!')
                    print('bạn có muốn tra menu nữa không (không thì nhấn q để thoát) ?')
                    tiep = input().lower()
                    if tiep == 'q' :
                        print('thoát chương trình quản lý công việc !')
                        break
                    else:
                        continue
            cong_viec.append({'ten': ten_cv, 'gio': gio_cv})
            print('thêm công việc thành công!')
            print('danh sách công việc hiện tại là:')
            print(cong_viec)
            print('bạn có muốn tra menu nữa không (không thì nhấn q để thoát) ?')
            tiep = input().lower()
            if tiep == 'q' :
                print('thoát chương trình quản lý công việc !')
                break
            else:
                continue

    elif chon == '2':
            tenxoa = input('hãy nhập tên công việc muốn xoá: ')
            for cv in cong_viec:
                if cv['ten'] == tenxoa:
                    cong_viec.remove(cv)
                    print('xoá công việc thành công!')
                    print('danh sách công việc hiện tại là:')
                    print(cong_viec)
                    print('bạn có muốn tra menu nữa không (không thì nhấn q để thoát) ?')
                    tiep = input().lower()
                    if tiep == 'q' :
                        print('thoát chương trình quản lý công việc !')
                        break
                    else:
                        continue
            else:
                print('công việc không tồn tại!')
                print('bạn có muốn tra menu nữa không (không thì nhấn q để thoát) ?')
                tiep = input().lower()
                if tiep == 'q' :
                    print('thoát chương trình quản lý công việc !')
                    break
                else:
                    continue
    elif chon == '3':
            print('danh sách công việc hiện tại là:')
            for cv in cong_viec:
                print(f" - {cv['ten']} vào lúc {cv['gio']} giờ")
            print('bạn có muốn tra menu nữa không (không thì nhấn q để thoát) ?')
            tiep = input().lower()
            if tiep == 'q' :
                print('thoát chương trình quản lý công việc !')
                break
            else:
                continue
    elif chon == '4':
            ten_thay_doi = input ('hãy nhập tên mà bạn muốn thay đổi giờ :')
            for i in cong_viec :
                if i ['ten'] == ten_thay_doi :
                    gio_moi = int(input('hãy nhập giờ mới cho công việc trên :'))
                    i ['gio'] = gio_moi
                    print('thay đổi giờ cho công việc thành công :')
                    print(cong_viec)
                    print('bạn có muốn tra menu nữa không (không thì nhấn q để thoát) ?')
                    tiep = input().lower()
                    if tiep == 'q' :
                        print('thoát chương trình quản lý công việc !')
                        break
                    else:
                        continue
            else:
                print('công việc không tồn tại!')
                print('bạn có muốn tra menu nữa không (không thì nhấn q để thoát) ?')
                tiep = input().lower()
                if tiep == 'q' :
                    print('thoát chương trình quản lý công việc !')
                    break
                else:
                    continue
    elif chon == '5':
            print('thoát chương trình quản lý công việc!')
            break
    else:
            print('lựa chọn không hợp lệ, vui lòng thử lại!')
            print('-----------------------------------')
            print('bạn có muốn tra menu nữa không (không thì nhấn q để thoát) ?')
            tiep = input().lower()
            if tiep == 'q' :
                print('thoát chương trình quản lý công việc !')
                break
            else:
                continue