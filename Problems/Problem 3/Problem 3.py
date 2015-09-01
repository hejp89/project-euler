import math
import time

primes = []

def is_prime(n, primes):
	if n <= 1:
		return False
	for i in range(len(primes)):
		if n % primes[i] == 0:
			return False
	return True

found = False
n = 600851475143
i = 2
primes.append(i)
start_time = time.time()

while not found:
	i += 1
	if is_prime(i, primes):
		primes.append(i)
		if n % i == 0:
			n /= i
		if n == 1:
			found = True
		
print(time.time() - start_time)

def compute():
	n = 600851475143
	while True:
		k = smallest_prime_factor(n)
		if k == n:
			return str(n)
		n //= k


def smallest_prime_factor(x):
	for i in range(2, int(math.sqrt(x)) + 1):
		if x % i == 0:
			return i
	return x


start_time = time.time()
print(compute())
print(time.time() - start_time)