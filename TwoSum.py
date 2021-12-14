
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

def twoSum_1(nums, target):
	for i in range(len(nums)):
		# if target >= nums[i]:
			for j in range(len(nums) - 1):
				if ((i != j) and (target - nums[i] == nums[j])):
					return [i, j]


def twoSum(self, nums, target):
	hash_map = dict()
	for i in range(len(nums)):
		num = nums[i]
		complement = target - num
		if complement not in hash_map:
			hash_map[num] = i
		else:
			return [hash_map[complement], i]

print(twoSum([2,7,11,15], 9))

assert twoSum([2,7,11,15], 9) == [0, 1]