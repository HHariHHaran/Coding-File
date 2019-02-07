a=raw_input()
b=a[::-1]
if a==b:
	print "0"
else:
	s=0
	l=[]
	for i in range(0,len(a)):
		l.append(a[i])
	z=[]
	for i in l:
		if l.count(i)==1:
			z.append(i)
	print len(z)
