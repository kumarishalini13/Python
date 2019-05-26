#duplicate in list
arr = [1,3,2,4,5,1]
arr1 = sorted(arr)
n = len(arr1)
count=0
if (n==1):
    print("girl")
elif (n> 0):
    for i in range(n-1):
        if (arr1[i] == arr1 [i+1]):
            print("boy")
            break
        else:
            count += 1
if(count>1):
    print("girl")