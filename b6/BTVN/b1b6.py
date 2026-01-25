n = int(input("Nhập vào số nguyên dương n: "))
sum = 0
for i in range(n + 1):
    if i % 2 == 0:
        sum += i
print("Tổng các số chẵn từ 1 đến", n, "là:", sum)