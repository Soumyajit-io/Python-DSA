l=[3, 5, 6, 3, 4, 6, 2, 8,1]
x=7
for i in range(0,len(l)-1):
    for j in range (i+1,len(l)):
        if l[i]+l[j] == x:
            print(i,j)