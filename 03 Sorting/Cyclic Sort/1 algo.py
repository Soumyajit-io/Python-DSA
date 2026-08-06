l = [5,1,3,4,2]

n=len(l)
print(l)
i=0
while(i<n):
    correctidx=l[i]-1
    if i==correctidx :
        i+=1
    else:
        l[i],l[correctidx]=l[correctidx] , l[i]
        print(l)
print(l)


