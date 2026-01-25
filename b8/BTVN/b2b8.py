n = int(input("Nhập tháng tùy chọn: "))
if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    print("Đây là tháng có 31 ngày")
else:
    if n == 4 or n == 6 or n == 9 or n == 11:
        print("Đây là tháng có 30 ngày")
    else:
        if n == 2:
            print("Tháng này có 28 hoặc 29 ngày")
        else:
            print("Không phải tháng trong năm")