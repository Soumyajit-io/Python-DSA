m=[[1,2,3],[4,5,6],[7,8,9]]
r=3
c=3
print(m)
for i in range(0,r):
    for j in range(0,c):
        if i!=j and j>i:
            m[i][j],m[j][i]=m[j][i],m[i][j]
print(m)
