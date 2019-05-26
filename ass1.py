ar = [10,3,5,6,2]
ar1 = []
result=1
for i in range(len(ar)):
        result=1
        for j in range(len(ar)):
                if(i==j):
                        continue
                else:
                        result = result*ar[j]
        ar1.append(result)
print(ar1)

