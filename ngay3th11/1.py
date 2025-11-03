def tkb(*monhoc):
    print("Môn học của tôi là " , monhoc[0])
    print("Môn học của tôi là " , monhoc[1])
tkb("Toán","Văn","Anh")
def tinhtong(*giatri):
    a = 0
    for i in giatri:
        a += i
    print(a)
tinhtong(1,2,3,4,5,6,7,8,9,10)
def thongtin(**tt):
    print("Tên tôi là : ", tt["ten"])
    print("Tuổi tôi là : ", tt["tuoi"])
    print("Địa chỉ tôi là : ", tt["diachi"])
thongtin(ten="Nguyễn Văn quân", tuoi=18, diachi="Hà Nội")