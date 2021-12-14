"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Example 3:

Input: nums = []
Output: []

Example 4:

Input: nums = [-1]
Output: ["-1"]

Example 5:

Input: nums = [0]
Output: ["0"]
-3 -1 1 2 
Алгоритм:
1. Условие: текущий элемент >= предыдущего (массив отсортирован) и их разность <= 1
2. Если текущий элемент не удовлетворяет условию
	-> беру предыдущий и добавляю в конец интервала вместе с символом "->" 
	-> текущий элемент добавляю в начало следующего интервала
3. Граничный случай: 1 элемент в массиве -> вывести этот элемент
4. Граничный случай: разность <= 1 в конце массива
5. пустой массив -> ""
6. массив из 1го элемента -> ["этот элемент"]
7.Случай, когда разность между соседними элементами массива всегда = 1
8. Разность > 1 слева и справа от текущего элемента
0, 1, 2, 3, 4 ->  ["0->4"]

0 1 2 4 5 7 -> 
[0, 2][4, 5][7]

0,2,3,4,6,8,9 - > [0][2, 4][6][8,9]

"""

def	summary_ranges(arr):
	if len(arr) == 0:
		return []
	if len(arr) == 1:
		return [str(arr[0])]
	res = [str(arr[0])]
	j = 0
	for i in range(1, len(arr)):
		if arr[i] - arr[i - 1] > 1:
			if i > 1 and arr[i - 1] - arr[i - 2] == 1:
				res[j] += "->" + str(arr[i-1])
			res.append(str(arr[i]))
			j += 1
		else:
			if i == len(arr) - 1:
				if arr[i] - arr[i - 1] == 1:
					res[j] += "->" + str(arr[i])
	return res

assert summary_ranges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
assert summary_ranges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
assert summary_ranges([0,2]) == ["0","2"]
assert summary_ranges([0,1]) == ["0->1"]
assert summary_ranges([0,1,3]) == ["0->1", "3"]
assert summary_ranges([]) == []
assert summary_ranges([-1]) == ["-1"]
assert summary_ranges([0]) == ["0"]
