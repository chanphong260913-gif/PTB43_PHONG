danhsachdiem = []
# thêm điểm
sobaikiemtra = int(input("Nhập số bài kiểm tra: "))
while sobaikiemtra <= 0:
    sobaikiemtra = int(input("Nhập lại số bài kiểm tra > 0: "))

for i in range(sobaikiemtra):
    diem = float(input(f"Nhập điểm bài {i + 1}: "))
    while diem < 0:
        diem = float(input("Nhập lại điểm hợp lệ: "))
    # thêm vào danh sách
    danhsachdiem.append(diem)

print("Danh sách điểm", danhsachdiem)
#1. Sắp xếp danh sách điểm số theo chiều tăng dần
danhsachdiem.sort(reverse=False)
print("Danh sách diemer sau khi sort", danhsachdiem)
#2. Xoá số điểm nhỏ nhất (Nếu có hai số điểm nhỏ nhất thì xoá cả hai)
if (sobaikiemtra == 1): print("Không thể xóa do danh sách có 1 phần tử")
else:
    diemnn = min(danhsachdiem)
    # lập tới khi xóa hết điểm nhỏ nhất(nếu trùng)
    while diemnn in danhsachdiem:
            danhsachdiem.remove(diemnn)
print("Đã xóa điểm nhỏ nhất")
#3. Xuất danh sách điểm sau khi đã xử lý yêu cầu 1 và 2

#4. Đếm số lượng điểm lớn hơn hoặc bằng 8 và xuất ra màn hình
counter = 0
for vaule in danhsachdiem:
     if value >= 8: counter+=1
print("Số lượng ddiemeer >= 8:", counter)

danhsachdiemluonlonhon8 = [value for value in danhsachdiem if value >= 8]
print(len(danhsachdiemlonhon8)) # độ dài danh sách điểm >