def primefac(num):
	primes = []
	for each in range(2,num):
		for i in range(2, each):
			if (each%i)==0:
				break
		else:
			primes.append(each)
			
	thefac= []
	for eachnum in primes:
		if num%eachnum==0:
			thefac.append(eachnum)
	
	print(f'The largest prime factor of {num} is {str(thefac[-1])}')
	
	
	
primefac(13195)
primefac()