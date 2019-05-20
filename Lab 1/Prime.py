def prime(n):
	count = 0
	for i in range(2, n):
		if n % i == 0:
			count += 1
	
	if count == 0:
		return 'Prime'
	else:
		return 'Not Prime'


print(prime(13))
print(prime(18))
print(prime(56))
print(prime(111))