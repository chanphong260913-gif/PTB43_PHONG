# tạo tam giác vuông * với n dòng (n > 1)
# input n
n = input("Số dòng > 1: ") #srt
n = int(n) # int
if (n <2):
    print("Số dòng phải lớn hơn 1")
else:
    # tạo tam giác vuông *
    for i in range(1, n+1):
        print("*"*i)