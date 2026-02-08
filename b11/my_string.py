
#-----67-----67-----67-----67-----67-----67----- 
# khai báo sâu kí tự
chuoirong = ""
fullname = "Ma Ky Ky"
#-----67-----67-----67-----67-----67-----67-----
# độ dài chuỗi
print(len(chuoirong))
print(len(fullname))
#-----67-----67-----67-----67-----67-----67-----
# duyệt xâu
for chart in fullname:
    print(chart, end="")

for index in range(len(fullname)):
    # truy cập phần tử
    print(f"{index}: {fullname[index]}")
#-----67-----67-----67-----67-----67-----67-----  
# + xâu kí tự
sentence = "My fullname is" + fullname + "."
print(sentence)
#-----67-----67-----67-----67-----67-----67-----
# xâu con
firstname = "Ma"
lastname = "diep"
#-----67-----67-----67-----67-----67-----67-----
# tìm  xâu con trong danh sách (in)
print(firstname in fullname) # true
print(lastname in fullname) # false
#-----67-----67-----67-----67-----67-----67-----
# chỉnh kiểu cho string
print(fullname.lower()) # chuyển hết kí tự thành chữ thường
print(fullname.upper()) # chuyển hết kí tự thành chữ hoa
print(fullname.capitalize()) # viết hoa chữ cái đầu tiên trong str
#-----67-----67-----67-----67-----67-----67-----
# tìm vị trí xâu con (find)
dindex = fullname.find("d")
print(dindex) # không có trả về -1
# NOTE: find(kí tự cần tìm, start, stop)
kindex = fullname.find("K", 4) # nếu tùng kí tự thì lấy kí tự đầu tiên (start, stop)
print(kindex)
#-----67-----67-----67-----67-----67-----67-----
# str -> list (split)
namelist = fullname.split(" ")
print(namelist)
#-----67-----67-----67-----67-----67-----67-----
# thay đổi phần tử (giá trị)
# replace(giá trị cần thay, giá trị mới, số lượng cần thay) -> hàm có return
# NOTE: nếu không có <số lượng cần thấy> -> sửa hết
newname = fullname.replace("Ky","Diep", 1)
print(newname)