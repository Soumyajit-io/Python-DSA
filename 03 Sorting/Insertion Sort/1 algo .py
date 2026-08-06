arr = [5,4,3,2,1]
n = len(arr)
for i in range(1,n):
    j=i
    while(j>=1 and arr[j-1]>arr[j]):
        arr[j],arr[j-1]=arr[j-1],arr[j]
        j-=1

print(arr)