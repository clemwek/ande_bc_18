def gen_prime(upper_limit):
    """
    A function that generates prime numbers

    First check if its greater than 2 since 2 is the smallest prime number
    create list to hold the variables
    Then iterate through integers btn 2 and n
    since 2 is the first prime number we add it to the prime list
    the for loop checks if it has divisors less than its square root if it finds its added in not_prime number
    the remaining numbers are primes and are saved in prime list
    am using Sieve of Eratosthenes formula---where you go through odd numbers and ruling out if they have divisors
    :param upper_limit:  int
    :return: list of prime numbers
    """
    try:
        upper_limit = int(upper_limit)
        if upper_limit >= 2:
            not_prime = []
            prime = []
            for i in range(2, upper_limit + 1):
                if i not in not_prime:
                    prime.append(i)
                    for j in range(i * i, upper_limit + 1, i):
                        not_prime.append(j)
            return prime
        else:
            return "prime numbers are positive and greater than one!"
    except ValueError:
        return 'Wrong entry'
    except TypeError:
        return 'Wrong entry'
