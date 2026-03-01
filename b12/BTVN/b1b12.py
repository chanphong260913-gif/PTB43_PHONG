s = input("Nhập chuỗi: ")
def tao_xau(s):
    i = 1
    while i <= len(s):
        print(s[:i])
        i += 1

# Gọi hàm
tao_xau(s)
