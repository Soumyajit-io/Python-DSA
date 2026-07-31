def partition(arr,lo,hi):
    print("the arr : ",arr)
    count = 0
    pvtele = (lo+hi)//2
    print("pvtele:", arr[pvtele])
    pvtidx = -1
    for i in range(lo,hi+1):
        if i == (lo+hi)//2:
            continue
        if arr[i]<arr[pvtele]:
            count+=1
    print(count)
    pvtidx = count + lo
    arr[pvtele],arr[pvtidx] = arr[pvtidx],arr[pvtele]
    print("after swap",arr)
    i=lo
    j=hi
    while i < pvtidx and j > pvtidx:
        if arr[i] <= arr[pvtidx]:
            i += 1
        elif arr[j] <= arr[pvtidx]:   # ✅ elif, not a separate if
            j -= 1                     # ✅ swap condition is now correct
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

     
    print("final: ",arr)

    
    return pvtidx

def quickSort(arr,lo,hi):
    if lo>=hi : return
    pvtidx = partition(arr,lo,hi)

    quickSort(arr,lo,pvtidx-1)
    quickSort(arr,pvtidx+1,hi)

    print("final : ",arr)

l = [5,9,1,80,99,-8,99999,-89,830,20,9,44,70,1,23]
quickSort(l,0,len(l)-1)
print(l)