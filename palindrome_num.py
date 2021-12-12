def	isPalindrome(num):
	str_num = str(num)
	for i in range(len(str_num) // 2):
		if str_num[i] != str_num[len(str_num) - i - 1]:
			return False
	return True

assert isPalindrome(-123) == False
assert isPalindrome(121) == True
assert isPalindrome(1) == True
assert isPalindrome(12) == False
assert isPalindrome(3113) == True
assert isPalindrome(31013) == True