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

def sum_of_primes(num):
    i = 2
    acc = 0

    while i < num:
        if isPrime(i):
            acc += i
        i += 1
    return acc

print (sum_of_primes(2000000))