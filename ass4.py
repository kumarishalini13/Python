ar = [1,1,1,2,2,2,3,3]
ar1 = sorted(ar)
temp = ar1[0]
count = 0
ar2 = []
for i in range(len(ar)):
    if(ar[i]==temp):
        count +=1
    else:
        temp = ar[i]
        ar2.append(count)
temp1 = ar2[0]
for i in range(1,len(ar2)):
    if(ar2[i]==1):
        print("False")
    elif (temp1 != ar2[i]):
        print("False")
    else:
        print("True")
