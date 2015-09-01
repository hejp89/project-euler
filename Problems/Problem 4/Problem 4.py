# Problem 4: determine the largest palindrome made from the product of two 3-digit numbers

def problem4():
	current = 0
	for i in range(999, 100, -1):
		for j in range(999, i - 1, -1):
			if is_palindrome(i * j) and i * j > current:
				current = i * j

	return current

def is_palindrome(num):
	return str(num) == str(num)[::-1]

if __name__ == '__main__':
	print(problem4())