i=int(input())
a=input()
a1=input()
a2=[]
for i in range(0,len(a)):
   if a[i]==a1[i]:
      a2.append(a[i])
a=''.join(a2)        
print(a)
