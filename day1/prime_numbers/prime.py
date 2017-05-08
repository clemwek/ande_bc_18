"""A function that generates prime numbers"""
"""
...First check if its greater than 2 since 2 is the smallest prime number
...create list to hold the variables
...Then iterate through integers btn 2 and n
......since 2 is the first prime number we add it to the prime list
......the for loop checks if it has divisors less than its squere root if it finds its added in not_primr number
...the remaining numbers are primes and are saved in prime list
am using Sieve of Eratosthenes formula---where you go thro' odd numbers and rulling out if they have divisors
"""
def gen_prime(n):
	try:
		n = int(n)
		if n >= 2:
			not_prime = []
			prime = []
			for i in range(2, n+1):
				if i not in not_prime:
					prime.append(i)
					for j in range (i*i, n+1, i):
						not_prime.append (j)
			return prime

		else :
			return "prime numbers are positive and greater than one!"

	except Exception as e:
		return 'Wrong entry'
		
if __name__ == "__main__":
    print (gen_prime(200))