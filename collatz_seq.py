def collatz(num):
    startingNum = 1
    
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1
        startingNum += 1
    return startingNum
