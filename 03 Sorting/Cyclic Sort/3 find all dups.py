def findDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        i=0
        l=[]
        while(i<n):
            ci = nums[i]-1
            if i == ci :
                print("arr: " ,nums)
                i+=1
            elif(nums[i]==nums[ci]):
                i+=1
            else:
                print("arr: " ,nums)
                nums[i],nums[ci]=nums[ci],nums[i]
        for i in range(n):
             if nums[i]-1!=i:
                  l.append(nums[i])
        return l

print(findDuplicates([4,3,2,7,8,2,3,1]))
# print(findDuplicates([2,1,2]))