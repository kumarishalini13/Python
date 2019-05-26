#multiplication of previous and next

arr = [2,3,4,5,6,7]
n= len(arr)
x = arr[0]
if (n==1):
    arr = arr
elif (n ==2):
    arr[0]= arr[0]*arr[1]
    arr[1]= arr[0]*arr[1]
else:
    temp1 =arr[0]*arr[1]
    temp2 = arr[n-1]*arr[n-2]
    for i in range(1,n-1):
        temp = arr[i]
        arr[i] = x * arr[i+1]
        x = temp
    arr[0]= temp1
    arr [n-1] = temp2
print(arr)




