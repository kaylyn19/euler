def triangularNumber(num):
  result = num * (num + 1) / 2
  return int(result)

def factors(length):
    i = 1
    while True:
      result = []
      triNum = triangularNumber(i)

      for factor in range(1, triNum):
        if triNum % factor  == 0:
          result.append(factor)
        if len(result) == length:
          return triNum
      i += 1

print(factors(500))