def isPrime(num):
    prime = [0, 2, 3]
    if num in prime:
        return True
    
    if num % 2 == 0:
        return False
    # if the number is not divisible by 2, check the odd numbers

    counter = 3
    while (counter ** 2 <= num):
        if num % counter == 0:
            return False
        else:
            counter += 2

    return True

def prime_factor(num):
    i = 0
    largest_prime_factor = 0
    while i < num:
        if isPrime(i):
            largest_prime_factor = i
        i += 1
    return largest_prime_factor        

print (prime_factor(13195))