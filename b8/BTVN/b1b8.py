a = int(input("Nhập số nguyên 1 bất kì: "))
b = int(input("Nhập số nguyên 2 bất kì: "))
c = int(input("Nhập số nguyên 3 bất kì: "))
if a > 0 and b > 0 and c > 0:
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Đây là hình tam giác")
    else:
        print("Đây không phải là hình tam giác")
else:
    print("Chỉ nhập số nguyên dương")