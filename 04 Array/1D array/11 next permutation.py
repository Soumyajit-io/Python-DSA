# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

class Solution(object):
    def nextPermutation(self, nums):
        def reversepart(l,x,y):
            i = x
            j = y
            while(i<j):
                l[i] ,l[j] = l[j],l[i]
                i+=1
                j-=1
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx = -1
        n=len(nums)
        # 1. finding pivot element
        for i in range(n-2,-1,-1):
            if (nums[i]<nums[i+1]):
                idx =i
                break
        # if no pivot --> reverse
        if(idx==-1):
            nums.reverse()
            return
        
        for i in range(n-1,idx,-1):
            if nums[i] > nums[idx]:
                nums[idx], nums[i] = nums[i], nums[idx]
                break


        reversepart(nums,idx+1,n-1)
        
        
        




        