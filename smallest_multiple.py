'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def smallest_multiple():
  i = 1
  divisible = 'true'
  while True:
    for n in range(1, 21):
      if i % n == 0:
        if n == 20:
          print ('done')
          return i
      else:
        i += 1
        break        

  # divisible = []
  # while True:
  #   for ind in range(1, 21):
  #     if i % ind == 0:
  #       divisible.append('true')
  #     else:
  #       divisible.append('false')
  #   if 'false' in divisible:
  #     divisible = []
  #     i += 1
  #   else:
  #     return i

print(smallest_multiple())