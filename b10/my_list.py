danhsach1 = [1, "a", "abc123", 12.3, False]

#-----67----------67----------67----------67-----
# duyệt danh sách
for i in range(len(danhsach1)):
	print(danhsach1[i])

# dùng khi không cần index
for value in danhsach1:
	print(value)

#-----67----------67----------67----------67-----
# thêm mới phần tử
# append(value): thêm vào cuối phân tử
danhsach1.append(100)
print(danhsach1)
#insert(index, value): thêm vào vị trí index
danhsach1.insert(len(danhsach1) -1, "new")
print(danhsach1)

#-----67----------67----------67----------67-----
# sửa phần tử
danhsach1[4] = "updated item"
print(danhsach1)

#-----67----------67----------67----------67-----
# xóa phần tử
# pop(): xóa ở vị trí cuối cùng của danh sách => trả về phần tử bị xóa
delitem = danhsach1.pop()
print(f"{delitem} đã được xóa khỏi danh sách {danhsach1}")
#pop(index): xo ở vị trí index => trả về phần tử bị xóa
delitem1 = danhsach1.pop(-1)
print(f"{delitem1} đã được xóa khỏi danh sách {danhsach1}")
# remove(value): xóa phần tử có value trùng khớp(nếu có nhiều phần tử giống => xóa ở trái)
# Note: remove trả về lỗi nếu không có phần tử này
print(danhsach1)
# clear(): xóa hết danh sách
print(danhsach1.clear())
#-----67----------67----------67----------67-----
# sắp xếp danh sách
# sort(reverse=?): nếu ? là False: tăng dần | ? là True: giảm dần
# NOTE: nếu muốn sắp xếp => cùng kiểu dữ liệu trong danh sách
danhsach2 = ['a','m','A','X','-']

danhsach2.sort(reverse=True)
print(danhsach2) # giảm dần
danhsach2.sort(reverse=False)
print(danhsach2) # tăng dần