# input: dãy điểm (0 -> 10, cach = " ")
daydiem = input("Nhập dãy điểm (0 -> 10, cach = " "): ")
diemparts = daydiem.split(' ')
# nhập sai format (không phải số hoặc ngoài khoảng 0 - 10)
while True:
    vald = True
    for diem in diemparts:
        diem = float(diem)
        if not (0 <= diem <= 10):
            valid = False
            break

if not valid:
    daydiem = input("Nhập lại dãy điểm (0 -> 10, cach = " "): ")
    diemparts = daydiem.strip()# cắt hết khoảng trắng đầu dưới
    diemparts = daydiem.split(' ')
else: count10 = 0
    # output: số điểm 10
    for diem in diemparts:
        diem = float(diem)
        if diem == 10:
            count_10 += 1

print(f"Số điểm 10 là: {count10}") if count 10 > 0 else print("Không có điểm 10")