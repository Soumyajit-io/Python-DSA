def subsets(nums,temp,res,idx):
    if len(nums)==idx:
        res.append(temp[:])
        return

    subsets(nums,temp,res,idx+1)
    temp.append(nums[idx])
    subsets(nums,temp,res,idx+1)
    temp.pop()

nums = [1,2,3,4,5]
temp=[]
res = []
idx=0
subsets(nums,temp,res,idx)

print([x for x in res if len(x)==3])