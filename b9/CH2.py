tong = 0
for so in range(2, 100):
    dem_uoc = 0
    for i in range(1, so + 1):
        if so % i == 0:
            dem_uoc += 1
    if dem_uoc == 2:
        print(so)
        tong = tong + so

print("Tổng là:", tong)