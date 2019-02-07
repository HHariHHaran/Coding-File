def x(a, b):
	a.sort() 
	i = 0
	j = b-1
	while (i < j): 
		print(a[j], end =" ")
		j-= 1
		print(a[i], end =" ")
		i+= 1
	if (n % 2 != 0):
		print(a[i]) 
a = [10, 102, 49, 86, 757, 105] 
b = len(r)
x(a, b)
