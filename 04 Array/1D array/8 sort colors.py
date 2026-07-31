l = [0,1,1,2,0,1,0,1,0,1,2,2]
lo = 0
mid=0
hi=len(l)-1

while(mid<=hi):
    if (l[mid]==0):
        l[lo],l[mid]=l[mid],l[lo]
        lo+=1
        mid+=1
        
    elif(l[mid]==2):
        l[hi],l[mid]=l[mid],l[hi]
        hi-=1
    else:
        mid+=1
    print(l)
print(l)
print(mid,hi)