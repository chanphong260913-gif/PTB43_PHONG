s = int(input("Nhập số giây: "))

gio = s // 3600
s = s % 3600
phut = s // 60
giay = s % 60
print(gio, "giờ", phut, "phút", giay, "giây")
