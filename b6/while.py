# WHILE: vòng lập vô hạn
# while <điều kiện> lặp lại cho đến khi điều kiện sao

# nhập số nghuyên chẵn a -----------------
a = input("nhập số nguyên chẵn a: ")
while(int(a) % 2 != 0):
	a = input("Nhập lại một số chẵn")
print("Số chẵn a là", a)