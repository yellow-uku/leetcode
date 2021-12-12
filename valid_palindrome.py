"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

def	my_isalpha(s):
	for char in s:
		if ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or ord(char) > 122:
			return False
	return True

# def	isPalindrome(s):
# 	# убрала пунктуацию
# 	words = s.lower()
# 	if my_isalpha(s) == False:
# 		punctuation = ' ?,.;:#@'
# 		for char in punctuation:
# 			words = words.replace(char, '')
# 	print("start ->", words, "<- end", sep="")
# 	# проверка на полиндром
# 	for i in range(len(words) // 2):
# 		if words[i] != words[len(words) - i - 1]:
# 			return False
# 	return True

def	isPalindrome(s):
# завожу два указателя (так удобно не учитывать пунктуацию == скипать)
	l = 0
	r = len(s) - 1
	s = s.lower()
	# print(s[l].isalpha())
	while l < r:
		while l < r and not s[l].isalnum():
			l += 1
		while l < r and not s[r].isalnum():
			r -= 1
		if l < r and (s[l] != s[r]):
			return False
		else:
			l += 1
			r -= 1
	return True

# print(isPalindrome("race a car"))

assert isPalindrome("race a car") == False
assert isPalindrome("A man, a1 plan, a canal: P1anama") == True
assert isPalindrome(" ") == True
