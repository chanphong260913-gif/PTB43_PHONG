# hàm không có trả về (có print)
def hello():
    name = input("Nhập tên của bạn: ")
    print(f"Hi {name}!")

#---------------------------   
# hàm có trả về (return)
def sum_two_num():
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))

    return a + b
#---------------------------
# hàm có đầu vào (tham số - parameters)

def duplicate_str(s:str, n:int):
    return s * n
#---------------------------
# bien global
globalcount = 0
def counter_to_n(n: int):
    global globalcount # khai báo để có thể sử dụng biển global
    print(globalcount) # in ra biển global
    for i in range(n+1):
        globalcount += 1
    print(globalcount)
#---------------------------
# gọi lại hàm để chạy
if __name__ == "__main__":
    # phải đi kèm () mới chạy hàm 
    # hello()
    # print(sum_two_num())
    # print(duplicate_str("a", 233))
    counter_to_n(5)