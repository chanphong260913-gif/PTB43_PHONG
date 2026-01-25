mk = input("Nhập mật khẩu: ")
while True:
    nmk = input("Hãy nhập mật khẩu: ")
    if nmk == mk:
        print("Đăng nhập thành công")
        break
    else:
        print("Mật khẩu không chính xác")
