# Problem 14: 

def problem14(n):
	max_len = 0
	max_n = n
	for i in range(2, n):
		seq_len = collatz_sequence_length(i)
		if seq_len > max_len:
			max_len = seq_len
			max_n = i
	return [max_len, max_n]

def collatz_sequence_length(n):
	i = 0
	while n != 1:
		i += 1
		if n % 2 == 0:
			n = int(n / 2)
		else:
			n = 3 * n + 1
	return i

if __name__ == '__main__': 
    print(problem14(1000000))