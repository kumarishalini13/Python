#max from right:

l=[16,17,4,3,5,2]
n=len(l)
max = l[n-1]
l[n-1] = -1
for i in range(n-2,-1,-1):
   temp = l[i]
   l[i]= max
   if max < temp:
       max = temp
print(l)


