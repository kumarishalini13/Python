#sum of 2 element equal to k
ar = [1,2,3,4,6,9,10]
ar1= sorted(ar)
i = 0
j = len(ar)-1
k = 9
while(i<j):
    if(ar[i]+ar[j]==k):
        print(ar[i],ar[j])
        break
    else:
        if(ar[i]+ar[j]> k):
            j -= 1
        elif (ar[i]+ar[j]< k):
            i += 1
        else:
            print("not available")
