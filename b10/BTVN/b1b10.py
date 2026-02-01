n = int(input("Nhập số bài kiểm tra: "))
a = []
for i in range(n):
    diem = float(input("Nhập điểm: "))
    if diem < 0 or diem > 10:
        print("Điểm không hợp lệ!!!")
        exit()
    a.append(diem)
a.sort()
diemnn = a[0]
while diemnn in a:
    a.remove(diemnn)
print("Danh sách điểm sau khi xử lý:", a)
dem = 0
for diem in a:
    if diem >= 8:
        dem += 1
print("Số điểm lớn hơn hoặc bằng 8 là:", dem)
