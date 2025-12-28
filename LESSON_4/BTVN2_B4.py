# Nhập chiều cao
an = float(input("Nhập chiều cao của An (đơn vị: mét): "))
minh = float(input("Nhập chiều cao của Minh (đơn vị: mét): "))
lan = float(input("Nhập chiều cao của Lan (đơn vị: mét): "))

# So sánh và in kết quả
if an >= minh and an >= lan:
    print("An là người cao nhất với chiều cao", an, "mét.")
elif minh >= an and minh >= lan:
    print("Minh là người cao nhất với chiều cao", minh, "mét.")
else:
    print("Lan là người cao nhất với chiều cao", lan, "mét.")
