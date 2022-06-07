import typing
 
def find_subarray_1(arr: typing.List[int], needed_sum: int) -> typing.Optional[typing.List[int]]:
    result_table = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
 
    for i, _ in enumerate(result_table):
        for j, _ in enumerate(result_table[i][i:], start=i):
            try:
                result_table[i][j] = result_table[i][j - 1] + arr[j]
            except IndexError:
                result_table[i][j] = arr[j]
            
            if result_table[i][j] == needed_sum:
                return [i, j]
    
    return None

a = [1, -2, -3, 4, 5, 6] 
print(find_subarray_1(a, 6))

def prefix_sum(arr, i):
	prefix_sum = 0
	for j in range(0, i + 1):
		prefix_sum += arr[j]
	return prefix_sum

def	find_subarray_2(nums, x):
	hash = list()
	prefix_sum = 0
	for i in range(len(nums)):
		prefix_sum += nums[i]
		hash.append(prefix_sum)

	return prefix_sum

a = [1, 2, 3, 4, 5, 6]
 
print(find_subarray_2(a, 6))
print(find_subarray_2(a, 1))
print(find_subarray_2(a, 0))
print(find_subarray_2(a, 21))
print(find_subarray_2(a, 11))