T = [[0,1,1,1], [0,0,1,1], [0,0,1,1], [0,0,0,0]]
for r in T:
    for c in r:
        print(c,end = " ")
    print()
row = len(T)
col = len(T[0])
print(row,col)
for i in range(row):
    