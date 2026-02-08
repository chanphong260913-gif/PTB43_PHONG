d = input("Nhập danh sách điểm: ")
d_list = d.split(" ")
d10 = 0
for d in d_list:
    if d == "10":
        d10 += 1
if d10 > 0:
    print("Số điểm 10 bạn có là:", d10)
else:
    print("Bạn chưa có điểm 10")