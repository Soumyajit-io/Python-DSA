l=[0,4,7,3,1,6,2]
l=[0,1,2]
n=len(l)
print(l)
i=0
miss= n
while(i<n):
    correctidx=l[i]
    if i==correctidx or l[i]==n:
        i+=1
    else:
        print (i)
        print(correctidx)
        l[i],l[correctidx]=l[correctidx] , l[i]
        print(l)
print(l)
i=0
while(i<n):
    if(i==l[i]):
        i+=1
    else:
        miss =i
        i+=1

print(miss)