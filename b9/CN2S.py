tong_so_nt = 0
for so_can_xet in range(2, 101):
	la_so_nt = True
	for so_chia in range(2, (so_can_xet//2 + 1)):
		if so_can_xet % so_chia == 0:
			la_so_nt = False # chia hết cho 1 số # chính nó
			break

	# tính tổng số nguyên tố
	if la_so_nt == True:
		tong_so_nt += so_can_xet

print("Tổng Số nguyên tố (2 -> 100):", tong_so_nt)