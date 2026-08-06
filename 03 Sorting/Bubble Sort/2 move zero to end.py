def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n =len(nums)
        j=0
        i=0
        while(j<n):
            if nums[j]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
            j+=1
