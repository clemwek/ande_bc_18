def fizz_buzz (num):
	try:
		if num%3 == 0 and num%5 == 0:
			return 'FizzBuzz'
		elif num%3 == 0:
			return 'Fizz'
		elif num%5 == 0:
			return 'Buzz'
		else:
			return num
	except Exception as e:
		return 'invalid entry'
