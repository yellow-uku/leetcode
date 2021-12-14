"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false
"""
# не работает для очень длинной строки s
"""
1. l, r - границы рассматриваемого массива
2. l++, r-- - пока не дойду до неравных элементов
3. чекаю, будет ли полиндромом строка [l:r] и строка [l + 1:r + 1]
4. если хотя бы одна будет -> return true, иначе false
"""
def	isPalindrome(s, i, j):
	while i < j:
		if s[i] == s[j]:
			i += 1
			j -= 1
		else:
			return False
	return True

def	res(s):
	l = 0
	r = len(s) - 1
	while l < r:
		if s[l] == s[r]:
			l += 1
			r -= 1
		else:
			if isPalindrome(s, l, r - 1) == True or isPalindrome(s, l + 1, r) == True:
				return True
			else:
				return False
	return True

assert res("aba") == True
assert res("abca") == True
assert res("abc") == False
