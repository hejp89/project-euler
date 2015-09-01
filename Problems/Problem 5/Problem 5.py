def is_div(number, integers):
	for i in range(1, integers + 1):
		if number % i != 0:
			return False
	return True

n = 20
while not is_div(n, 20):
	n += 20

print(n)

# The best way is to decompose all of the numbers from 2 to 20 and determine the smallest set that 
# covers all numbers up to 20.