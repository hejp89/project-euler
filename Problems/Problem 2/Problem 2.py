# Problem 2: sum of all even Fibonacci numbers less than 4,000,000

def problem2():
	f_n = 1
	f_n1 = 2

	res = f_n1

	while f_n1 < 4000000:
		temp = f_n1
		f_n1 = f_n + f_n1
		f_n = temp
		res += f_n1 if f_n1 % 2 == 0 else 0

	return res

if __name__ == '__main__':
	print(problem2())