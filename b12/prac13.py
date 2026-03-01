def tinhluong(giolam, luonggio):
    tongluong = giolam*luonggio
    return tongluong

def inthongtinh(ten, giolam, luonggio,tongluong):
    print("Thông tin nhân viên:")
    print("Tên: ", ten)
    print("Số giờ làm:", giolam)
    print("Mức lương giờ: ", luonggio)
    print("Tổng tiền lương: ", tongluong)
tongluong = tinhluong(24, 30)
inthongtinh("PHOGNWKRKFLWEJFWEF", 24, 30,tongluong)