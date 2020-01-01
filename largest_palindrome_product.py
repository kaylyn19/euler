'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def largest_palindrome():
  for i in range(999, 900, -1):
    for j in range(999, 900, -1):
      product = i * j
      if str(product) == str(product)[::-1]:
        print ('i ==> ', i, 'j ==>', j)
        return 'product', product

print (largest_palindrome())