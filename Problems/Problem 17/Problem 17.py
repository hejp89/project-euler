# Problem 17: length of numbers written as words

def problem17(n):
	result = 0

	for i in range(1, n + 1):
		result += sum([1 if c != ' ' else 0 for c in number_to_words(i)])

	return result

# e.g. 623 -> six hundred and twenty three
def number_to_words(n):
	thousands = int(n / 1000) % 10
	hundreds = int(n / 100) % 10
	tens = int(n / 10) % 10
	units = n % 10

	parts = []

	if thousands > 0:
		parts.append(digit_to_word(thousands))
		parts.append('thousand')

	if hundreds > 0:
		parts.append(digit_to_word(hundreds))
		parts.append('hundred')
		if tens > 0 or units > 0:
			parts.append('and')

	if tens > 1:
		parts.append(tens_to_word(tens))

	if tens == 1:
		parts.append(digit_to_word(tens * 10 + units))

	if tens != 1 and units > 0:
		parts.append(digit_to_word(units))

	if len(parts) == 0:
		parts.append(digit_to_word(units))

	return ' '.join(parts)

def digit_to_word(n):
	digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 
			  'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	return digits[n]

def tens_to_word(n):
	tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	return tens[n]

if __name__ == '__main__': 
    print(problem17(1000))