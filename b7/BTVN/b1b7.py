n = int(input("Nhập số nguyên dương n: "))
tong = 0
so = 0
ket_qua = ""
while tong <= n:
    so = so + 1
    tong = tong + so
    ket_qua = ket_qua + str(so) + " "
print("Dãy số ngắn nhất là:", ket_qua)