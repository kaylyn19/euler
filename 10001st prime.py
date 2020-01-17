def isPrime(num):
    prime = [0, 1, 2, 3]
    if num in prime:
        return True
    
    if num % 2 == 0:
        return True
    # if the number is not divisible by 2, check the odd numbers

    counter = 3
    while (counter ** 2 <= num):
        if num % counter == 0:
            return False
        else:
            counter += 2

    return True

def x_th_prime(x_th):
    n = 0
    numToCheck = 1
    result = [2]

    while n < x_th:
        numToCheck += 2
        if isPrime(numToCheck):
            result.append(numToCheck)
            n += 1
        if len(result) == x_th:
            return result[-1]

print (x_th_prime(10001))