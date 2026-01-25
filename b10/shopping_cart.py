cart = []
funcs = [
	"0. In giỏ hàng",
	"1. Thêm vào giỏ",
	"2. Chỉnh sửa món hàng",
	"3. Xóa món hàng (theo index)",
	"4. Sắp xếp theo tên",
	"5. Thoát chương trình"
		]

# bắt đầu chương trình
print("---------------SHOPPING CART---------------")
while True:
	# in danh sách tính năng
	for value in funcs:
		print(value)
	# chọn 1 chức năng
	choice = int(input("Chọn 1 chức năng: "))
	# nếu không chọn đúng => báo lỗi
	while (choice > 5 or choice < 0):
		choice = int(input("Chọn 1 chức năng (0 => 5): "))
	# func 5:
	if choice == 5:
		print("Bye!")
		break

	# func 0:
	if choice == 0:
		if len(cart) == 0:
			print("Giỏ hàng rỗng")
			continue
		for i in range(len(cart)):
			print(f"{i}: {cart[i]}")
	# func 1:
	elif choice == 1:
		pass
	# func 2:
	elif choice == 2:
		pass
	# func 3:
	elif choice == 3:
		pass
	# func 4:
	elif choice == 4:
		pass