a=list(input())
b=list(input())
c=len(a)
e=len(b)
i=0
j=0
d=[]
while c>1:
   if a[i]==b[j]:
        d.append(a[i])
   j=j+1
   i=i-1
   c=c+1
print(e-len(d))
