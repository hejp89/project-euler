# Problem 1: sum of all integers less than 1000 that a divisible by 3 or 5

def problem1():
	x = 0

	# loop through 0-999 adding to x if the number is divible by 3 or 5
	for i in range(1000):
		x += (i % 3 == 0 or i % 5 == 0) * i

	return x

if __name__ == '__main__':
	print(problem1())