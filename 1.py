ar = [0,1,1,1,0,1,0,1,0,1,0,1]
prev_prev = -1
prev = -1
curr = -1
count = 0
max = 0
for i in range(len(ar)):
    if(ar[i]==0):
        curr = i
        prev = curr - prev - 1
        prev_prev = prev - prev_prev -1
        count = curr - prev -1
        if(count > max):
            max = count
print(max,prev)