# 大写字母 65 - 90
# 小写字母 97 - 122
# 字符转 ASCII ord()
# ASCII 转字符 chr()

# 转为小写
def conver_lowercase(chr1):
	num = ord(chr1)
	# 如果大写，转为小写
	if num >= 65 and num <= 90:
		num = num + 32
		return chr(num)
	return chr1
	

# 是否为字母
def is_letter(num):
	if (num >= 65 and num <= 90) or (num >= 97 and num <= 122):
		return True
	return False


def checkio(str):
	list1 = []
	list2 = []
	# 只保留字母
	for x in str:
		if is_letter(ord(x)):
			list1.append(x)

	# 计数
	for x in list1:
		count = 0
		for y in list1:
			if x == y or x == conver_lowercase(y):
				count += 1
		list2.append(count)

	# 找到 list 中最大的数字
	max_num = list2[0]	# 保存最大值
	index = 0			# 保存最大值位置的索引
	for i in range(len(list2)):
		# 如果有相等的，则取字母表靠前的
		if max_num == list2[i]:
			if ord(list1[index]) < ord(list1[i]):
				max_num = list2[index]
				index = index
			else:
				max_num = list2[i]
				index = i

		if max_num < list2[i]:
			max_num = list2[i]
			index = i

	return conver_lowercase(list1[index])

chr1 = input("输入字符串：")
print(checkio(chr1))

