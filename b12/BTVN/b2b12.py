d = input("Nhập số lượng diểm: ")
def dtb(d):
    tong = 0
    i = 0
    while i < len(d):
        tong += d[i]
        i += 1
    
    tong += ds[-1]
    heso = len(ds) + 1
    