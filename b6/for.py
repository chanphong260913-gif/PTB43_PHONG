# FOR: vòng lập hữu hạn
# range( start, stop, step)
# lặp lại trong khoảng từ <start> => <stop -1>, bước nhảy là <step> đơn vị
#-------67-------
# range(stop): lặp lại từ 0 => stop - 1, mặc định bước nhảy là 1
# range(start, stop): lặp lại từ start => stop - 1, mặc định bước nhảy là 1
# range(start, stop, step)

# countdown 10s happy new year
#import time
#
#for giay in range(10, 0, -1):
#	print(giay)
#	time.sleep(1)
#
#print("Happy new Year")
#
# vẽ tam giác -------67-------
canh = 10
for dong in range(canh+1):
	print(" " * (canh - dong) + "O "*dong)
	
print("Merry chistmas")