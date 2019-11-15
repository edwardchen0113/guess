import random
s = input('請輸入隨機數字起始值：')
e = input('請輸入隨機數字結束值：')
s = int(s)
e = int(e)
r = random.randint(s, e)
i = 0
while True:
	num = input('請輸入數字')
	num = int(num)
	i += 1
	if num == r:
		print('你猜對了！')
		print('你猜了', i, '次！')
		break
	elif num > r:
		print('你的數字比答案大')
	elif num < r:
		print('你的數字比答案小')
	print('你猜了', i, '次！')