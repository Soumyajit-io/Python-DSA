def printt(arr,idx,maxx):
    if idx==len(arr): return maxx
    if arr[idx]>maxx:
        maxx = arr[idx]
    return printt(arr,idx+1,maxx)
def print2(arr,idx):
    if idx==len(arr): return -1
    return max(arr[idx],print2(arr,idx+1))


print(print2([1,2,3,4,99,6],0))