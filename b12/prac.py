import math
# hàm rút gọn phân số
def rut_gon_phanso(tu:int, mau:int):
    # tìm UCLN để chia cho tử và mẫu
    ucln = math.gcd(tu, mau)
    tu_moi = tu // ucln # chia lấy số nguyên
    mau_moi = mau // ucln
    return tu_moi, mau_moi

# gọi lại hàm để chạy
if __name__ = "__main__":
    print(rut_gon_phanso(6,21))