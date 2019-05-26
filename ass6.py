#mean and median
ar = [2,4,7,6,8]
l = len(ar)
sum = 0
for i in range(l):
    sum += ar[i]
mean = sum / l
print(mean)
x=l//2
ar1 = sorted(ar)
if(l%2 ==0):
    median = (ar1[x]+ar1[x-1])/2
else:
    median = ar1[x]
print(median)