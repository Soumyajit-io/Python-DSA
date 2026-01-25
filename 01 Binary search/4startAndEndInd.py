# find the first and ending index of target 

class Solution(object):
    def searchRange(self, nums, target):
        return [self.sbinary(nums, target), self.ebinary(nums, target)]

    def sbinary(self, nums, target):
        lo, hi = 0, len(nums) - 1
        ans = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                ans = mid
                hi = mid - 1   # keep going left
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

    def ebinary(self, nums, target):
        lo, hi = 0, len(nums) - 1
        ans = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                ans = mid
                lo = mid + 1   # keep going right
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return ans