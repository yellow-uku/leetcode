def sort_three(nums):
	if nums[0] > nums[1] and nums[0] > nums[2]:
		return nums[0]
	if nums[1] > nums[0] and nums[1] > nums[2]:
		return nums[1]
	if nums[2] > nums[1] and nums[2] > nums[0]:
		return nums[2]
print(sort_three([2, 3, 1]))