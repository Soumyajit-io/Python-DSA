# # Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==1:
            if target ==nums[0]: return 0
            else : return -1
        if len(nums)==2:
            if target ==nums[0]: return 0
            elif target ==nums[1]: return 1
            else : return -1

        lo = 0
        hi = len(nums)-1
        pvt =-1 #smallest
    #    finding pivot
        while(lo<=hi):
            mid = lo+(hi-lo)//2
            if nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]:
                pvt = mid 
                break
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                pvt = mid +1
                break
            elif (nums[mid]<nums[mid+1] and nums[mid]>nums[mid-1]) and nums[mid] > nums[hi]:
                lo = mid+1
            elif (nums[mid]<nums[mid+1] and nums[mid]>nums[mid-1]) and nums[mid] < nums[hi]:
                hi = mid-1
        
        # finding taregt
        if pvt ==0:
            lo = 0
            hi = len(nums)-1
        elif target>=nums[0]: 
            hi=pvt-1
            lo = 0
        else:
            lo = pvt
            hi = len(nums)-1
        
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if nums[mid]==target: return mid
            elif nums[mid]>target: hi = mid-1
            else: lo= mid+1    
        return -1
