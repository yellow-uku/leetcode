"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Алгоритм:
1. Проверяю, лежит ли элемент из t в s. Пробегаюсь по t
2. Если лежит - добавляю его в новую строку res
3. Пробегаюсь по res. Если какой-то из элементов из res не совпадает с s, то возвращаю false
"""

def	is_subsequence(s, t):
	res = ""
	j = 0
	if len(s) == 0:
		return True
	else:
		if len(t) == 0:
			return False
	for i in range(len(t)):
		if t[i] == s[j]:
			res += t[i]
			j += 1
			if j >= len(s):
				break
	if len(res) == 0:
		if len(s) == 0:
			return True
		else:
			return False
	for i in range(len(s)):
		if len(s) > len(res) or res[i] != s[i]:
			return False
	return True

# print(is_subsequence("abc", "ahbgdc"))
# print(is_subsequence("axc", "ahbgdc"))
# print(is_subsequence("aaaaa", "bbaaa"))
# print(is_subsequence("", "bbaaa"))
print(is_subsequence("b", "abc"))