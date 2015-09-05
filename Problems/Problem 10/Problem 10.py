# Problem 10: calculate the sum of all primes < 2,000,000

import math

def problem10(n):
	result = 0
	for i in range(2, n):
		if is_prime(i):
			result += i
	return result

def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False

	return True

if __name__ == '__main__':
	print(problem10(2000000))