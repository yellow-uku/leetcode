
def findNumbers1(nums):
	str_nums = list(map(str, nums))
	list_len = list(map(len, str_nums))
	list_res = [num for num, count in zip(str_nums, list_len) if count % 2 == 0]
	# print(list_res)
	return len(list_res)
print(findNumbers1([555,901,482,1771]))


def findNumbers2(nums):
	return(len([x for x in nums if len(str(x)) % 2 == 0]))

print(findNumbers2([12,345,2,6,7896]))