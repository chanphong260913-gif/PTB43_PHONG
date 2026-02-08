# input: dd/mm/yyyy
date_str = input("Nhập ngày tháng năm (dd/mm/yyy)")
date_parts = date_str.split('/')
# nhập sai format (thiếu 1 trong 3 phần)
while len(date_parts) != 3:
    date_str = input("Nhập lại ngày tháng năm (dd/mm/yyy)")
    date_parts = date_str.split('/')
# kiểm tra ngày / tháng/ năm có hợp lệ không
day = int(date_parts[0])
month = int(date_parts[1])
year = int(date_parts[2])

if not(1 <= day <= 31) or not (1 <= month <= 12) or year < 0:
    print("Ngày tháng năm không hợp lệ!")
else:
    # output: day dd, thang mm, nam yyyy
    print(f"Ngày {day:02d}, thang {month:02d}, nam {year}")