l = [1,2,3,6,5,9,20]

i = 0
j = len(l)-1

while(i<j):
    l[i] ,l[j] = l[j],l[i]
    i+=1
    j-=1
print(l)