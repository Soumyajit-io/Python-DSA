arr = [5,4,3,2,1]
n = len(arr)
for i in range(0,n-1):
    minn=i
    for j in range(i+1,n):
        if arr[j]<arr[minn]:
            minn = j

    arr[i],arr[minn]=arr[minn],arr[i]

print(arr)