# Problem 9: find integers a, b, c such that a^2 + b^2 = c^2 and a + b + c = 1,000

def problem9(n):
	
	for a in range(1, n):
		for b in range(1, n):
			c2 = a**2 + b**2
			if c2 == (n - a - b)**2: # Avoiding sqrt to work only with integers and therefore avoiding rounding issues
				return {'a': a, 'b': b, 'c': n - b - a}

	return None

if __name__ == '__main__':
	soln = problem9(1000)
	if soln != None:
		print(soln['a'] * soln['b'] * soln['c'])