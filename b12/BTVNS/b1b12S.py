# viết hàm in ra từng kí tự trong chuỗi
def print_str(s):
    for i in range(len(s)):
        for j in range(i + 1):
            print(s[j], end="")
        print()

print_str(input("Nhập chuỗi cần in: "))