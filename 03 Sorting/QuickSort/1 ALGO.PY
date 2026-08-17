def partition (arr, si , ei ):
    pivotele = arr[(si+ei)//2]
    count = 0
    n=len(arr)
    for i in range(si,ei+1):
        if i == (si+ei)//2: continue
        if arr[i]<=pivotele:
            count+=1

    pivotidx = count+si

    arr[pivotidx],arr[(si + ei) // 2]=arr[(si + ei) // 2],arr[pivotidx]

    i=si
    j=ei
    while(i<pivotidx and j >pivotidx):
        if arr[i]<=pivotele:
            i+=1
        if arr[j]>pivotele:
            j-=1
        elif (arr[i]>pivotele and arr[j]<=pivotele):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    return pivotidx

def qs(arr,si,ei):
    if si>=ei: return
    pi = partition(arr,si,ei)
    qs(arr,si,pi-1)
    qs(arr,pi+1,ei)

l = [2,1,3,9,-0,6,8,3,7,89,0,-9,6,-88]

print(l)
qs(l,0,len(l)-1)
print(l)