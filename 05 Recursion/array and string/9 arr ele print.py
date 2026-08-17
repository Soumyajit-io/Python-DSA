def printt(arr,idx):
    if idx==len(arr): return
    print(arr[idx])
    return printt(arr,idx+1)
    print("extra")


printt([1,2,3,4,99,6],0)