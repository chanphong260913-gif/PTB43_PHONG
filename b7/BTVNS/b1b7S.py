# input: n
# output: dãy số từ 1 -> (sum > n)
n = -1
while n <= 0:
	#neu n <= 0 thi yeu cau nhap lai
	n = int(input("Nhập n (n -> 0): "))

sum = 0
i = 0
print("Dãy số từ 1 đến khi tổng vượt qua n: ", end= '')
while sum <= n:
	sum += 1
	print(i, end= '')
	i += 1