"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution1:
	def findMaxConsecutiveOnes(self, nums):
		# i = 0   # конец посл-ти + 1
		j = 0   # начало посл-ти
		len_list = [0]
		if nums[0] == 1 and 1 == len(nums):
			len_list.append(1)
		if (len(nums) == 2 and nums[1] == 1):
			len_list.append(1)
		for i in range(1, len(nums)):
			if (nums[i - 1] == 1 and (nums[i] == 0 or i == len(nums) - 1)):
				if (i == len(nums) - 1 and nums[i] != 0):
					len_list.append(i - j + 1)
				len_list.append(i - j)
			if nums[i] == 1 and nums[i - 1] == 0:
				j = i
		
		# print(len_list)
		return (max(len_list))

class Solution2:
	def findMaxConsecutiveOnes(self, nums):
		count, res = 0, 0
		for i in range(len(nums)):
			if nums[i] == 1:
				count += 1
			else:
				if nums[i] == 0:
					res = max(res, count)
					count = 0
		res = max(res, count)
		return res
			
class Solution3:
	def findMaxConsecutiveOnes(self, nums):
		list_ones = ''.join([str(x) for x in nums]).split('0')
		return max(list(map(len, list_ones)))


def main():
	res1 = Solution1()
	res2 = Solution2()
	res3 = Solution3()
	print(res3.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1, 0]))
main()
