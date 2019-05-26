ar = [0,1,1,1,0,1,0,1,0,1,0,1]
start = -1
end = 0
zc = 0
max = 0
for i in range(len(ar)):
    if(ar[end]==0):
        zc += 1
    if(zc< 2):
        end += 1
    elif(zc>2):
        start += 1
        zc = 0
        position = end
        count = end - start
        if( count > max):
            max = count
print(count,position)
