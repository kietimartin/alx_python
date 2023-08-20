def is_prime(number):
    '''Checks if a number is prime
    
    variables : number
    
    return : True if number is prime and false otherwise
    '''

    if (number <= 0):
        return False
    for i in range(1, number):
        if number % i == 0:
            return False
    return True