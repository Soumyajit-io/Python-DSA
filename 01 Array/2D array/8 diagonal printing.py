m=[[1,2,3],
   [4,5,6],
   [7,8,9],
   [10,11,12]]

r = len(m) #4
c = len(m[0]) #3

for k in range(0,c):
    i=0
    j=k
    while(j>=0):
        print(m[i][j])
        i+=1
        j-=1
for k in range(1,r):
    i=k
    j=c-1
    while(j>=0 and i < r):
        print(m[i][j])
        i+=1
        j-=1