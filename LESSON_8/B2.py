import math
# input: a, b
a = 0
b = 0
while (a and b) == 0:
	a = int(input("Nhập tử số: "))
	b = int(input("Nhập mẫu số: "))
# tính bội chung nhỏ nhất
bcnn = math.lcm(a, b)
print(f"BCNN của {a} và {b} là: {bcnn}")
# rút gọn phân số (ucln)
print(f"Phân số ban đầu: {a}/{b}")
ucln = math.gcd(a, b)
a = a // ucln
b = b // ucln
print(f"Phân số rút gọn: {a}/{b}")
