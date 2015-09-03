# Problem 7: determine the 10001th prime number

import math
import time

def problem7(n):
	i_prime = 0
	i = 0
	while i_prime < n:
		i += 1
		if is_prime(i):
			i_prime += 1
		
	return i

def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False

	return True

if __name__ == '__main__':
	print(problem7(10001))