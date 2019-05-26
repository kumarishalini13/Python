ar = [2,0,1,4,5,3]
ar1=[]
for i in range(len(ar)):
    ar1.append(0)
for i in range(len(ar)):
    x = ar[i]
    temp = ar[x]
    ar1[x]=i
print(ar1)