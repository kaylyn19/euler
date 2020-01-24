def power(exp):
    return 2**exp

def add(exp):
    pwr = power(exp)
    splitPwr = list(str(pwr))
    acc = 0
    for i in range(0, len(splitPwr)):
        acc += int(splitPwr[i])
    return acc

print(add(1000))