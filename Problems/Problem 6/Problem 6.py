# Problem 6: determine (1 + 2 + ... + 100)^2 - (1^2 + 2^2 + ... + 100^2)

def problem6(n):
	tot = 0
	tot_2 = 0

	for i in range(n + 1):
		tot += i
		tot_2 += i ** 2


	return tot ** 2 - tot_2

if __name__ == '__main__':
	print(problem6(10)) # should be 2640 given in the problem
	print(problem6(100))