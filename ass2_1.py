l=[6,2,4,5,3,1]
n=len(l)
max = l[n-1]
l[n-1] = -1
for i in range(n-2,-1,-1):
   temp = l[i]
   l[i]= max
   if max < temp:
       max = temp
print(l)
