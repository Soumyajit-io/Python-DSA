# algo with optimised
arr =[4,3,2,1,6,-5,-9,-7]
flag = False
n = len(arr)
for i in range(0,n-1,1): # n-1 passes
    flag = False
    for j in range(0,n-1-i,1):
        if arr[j]>arr[j+1]:
            print(f"arr: {arr} j = {j} pass = {i+1}")
            arr[j],arr[j+1]=arr[j+1],arr[j]
            flag= True
    if not flag :
        break
print(arr)