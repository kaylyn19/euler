def pythagorean_triple():
	for c in range (0, 1000):
		# print('c ====>', c)
		for b in range(0, 1000 - c):
			# print('a and b ====>', b)
			for a in range(0, 1000 - c - b):
				# print('a ====>', a)
				if c + a + b == 1000:
					if a ** 2 + b ** 2 == c ** 2:
						print (a, b, c)
						return

print(pythagorean_triple())