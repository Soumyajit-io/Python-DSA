l = [1,2,3,6,5,9,20]
def reversepart(l:list,x,y):
    i = x
    j = y
    while(i<j):
        l[i] ,l[j] = l[j],l[i]
        i+=1
        j-=1
print(l)
reversepart(l,1,3)
print(l)