def sort_three(nums):
	a, b, c = nums[0], nums[1], nums[2]
	if a > b:
		a, b = b, a
	else:
		if b > c:
			b, c = c, b
			if a > b:
				a, b = b, a
	return [a, b, c]

assert sort_three([2, 3, 1]) == [1, 2, 3]
assert sort_three([1, 3, 2]) == [1, 2, 3]
assert sort_three([2, 1, 3]) == [1, 2, 3]
assert sort_three([1, 1, 1]) == [1, 1, 1]
assert sort_three([1, 2, 3]) == [1, 2, 3]