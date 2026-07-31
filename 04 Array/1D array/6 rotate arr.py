# rotate the givn arr by k steps 

def reversepart(l:list,x,y):
    i = x
    j = y
    while(i<j):
        l[i] ,l[j] = l[j],l[i]
        i+=1
        j-=1

l = [1,6,2,3,7,4,8]
n=len(l)
k = 20
if k>n :
    k=k%n
reversepart(l,0,n-1-k)
reversepart(l,n-k,n-1)
reversepart(l,0,n-1)
print(l)
