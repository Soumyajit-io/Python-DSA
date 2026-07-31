l = [1,1,0,1,0,1,1,0 ]

i=0
j=len(l)-1
while(i<j):
    if (l[i]==0):
        i+=1
    if (l[j]==1):
        j-=1
    if (l[i]==1 and l[j]==0):
        l[i],l[j] = l[j],l[i]
        i+=1
        j-=1
print(l)
    