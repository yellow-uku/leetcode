
def	remove_smiles(arr):
	res = ''
	i = 0

	while i < len(arr):
		while i + 1 != len(arr) and i + 2 != len(arr) and (arr[i:i+3] == ':-)' or arr[i:i+3] == ':-('):
			i += 2
			if arr[i] == ')':
				while i != len(arr) and arr[i] == ')':
					i += 1
			else:
				if arr[i] == '(':
					while i != len(arr) and arr[i] == '(':
						i += 1
		if i < len(arr):
			res += arr[i]
		i += 1
	return res

assert remove_smiles(":-))()abc:-(((") == "()abc"
assert remove_smiles(":-)))") == ""
assert remove_smiles(":-))():-))") == "()"
assert remove_smiles("abc:-(((") == "abc"
assert remove_smiles(":-(((abc") == "abc"
