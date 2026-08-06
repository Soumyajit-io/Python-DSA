m=[[1,2,3],
   [4,5,6],
   [7,8,9]]
r=len(m)
c=len(m)
for i in range(0,r):
    if i%2 ==0:
        for j in range(0,c):
            print(m[i][j])
    else:
        for j in range(c-1,-1,-1):
            print(m[i][j])