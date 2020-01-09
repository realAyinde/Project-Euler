def evenfib(num):
	fib=[]
	if num == 1:
		fib =[1]
	elif num == 2:
		fib =[1,2]
	elif num > 2:
		fib = [1,2]
		for i in range(num-2):
			fib.append(fib[-1]+fib[-2])
	evens = [each for each in fib if each%2==0 ]
	return sum(evens)
		
print(evenfib(10))