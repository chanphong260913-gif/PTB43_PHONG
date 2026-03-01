# tính điểm trung bình cho danh sách điểm
def tinhdiemtb(dsdiemstr):
    # chuyển string -> list
    dsdiem = dsdiemstr.split(" ")
    # chuyển hết phần tử sang float (<0/>10)
    for i in range(len(dsdiem)):
        dsdiem[i] = float(dsdiem[i])
        if (not (0 <= ds_diem[i] <= 10)):
            print("Danh sách biến ko hợp lệ")
            return # kết thúc hàm
        
    # tính trung bình
    result = sum(dsdiem, dsdiem[len(dsdiem) - 1])/ (len(dsdiem) + 1)
    return round(result, 1)

pint (tính điểm tb(input()))