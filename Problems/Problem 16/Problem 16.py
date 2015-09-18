# Problem 16: sum of the digits in 2**1000

def problem16(base, exponent):
	
	return sum([int(n) for n in str(base ** exponent)])

if __name__ == '__main__': 
    print(problem16(2, 1000))