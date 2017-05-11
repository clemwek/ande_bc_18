def fizz_buzz(num):
    """
    this function takes in a number and returns fizzbuzz,
    fizz or buzz if the number is divisible by 3 and 5, 3 
    or 5
    :param num: int
    :return: string
    """
    try:
        if num % 3 == 0 and num % 5 == 0:
            return 'FizzBuzz'
        elif num % 3 == 0:
            return 'Fizz'
        elif num % 5 == 0:
            return 'Buzz'
        else:
            return num
    except Exception as e:
        return e
