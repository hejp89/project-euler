# Problem 12: determine the first triangle number with 500+ divisors

import math

def problem12(n):
    i = 1
    while number_of_divisors(triangle_number(i)) < n:
        i += 1
    return triangle_number(i)
    
def triangle_number(n): 
    return int(n * (n + 1) / 2)
    
def number_of_divisors(n):
    result = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result += 2
    return result

if __name__ == '__main__': 
	print(problem12(500))