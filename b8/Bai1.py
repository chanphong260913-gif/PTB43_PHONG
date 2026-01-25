# n ? nguyên tố ( > 2, số nguyên)
n = -1
while n < 2:
	n = int(input("Nhập một số nguyên >= 2: "))
lasonguyento = True
for i in range(2, n//2 + 1):
	if n % i == 0:
	    lasonguyento = False
		

# in kết quả
if lasonguyento == False:
	print(f"{n} không phải là số nguyên tố")
else:
	print(f"{n} là số nguyên tố")
