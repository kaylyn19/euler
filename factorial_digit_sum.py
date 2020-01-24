def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def add(n):
    factorialRes = factorial(n)
    splitRes = list(str(factorialRes))
    acc = 0
    for i in range(0, len(splitRes)):
        acc += int(splitRes[i])
    return acc
print (add(100))