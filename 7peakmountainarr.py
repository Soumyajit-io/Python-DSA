# find peak elemets index in mountain arr
# 1,2,3,4,5,6,4,1

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lo =0 
        hi = len(arr)-1
        while(lo<=hi):
            mid = lo+(hi-lo)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1] : 
                return mid
            elif arr[mid] < arr[mid-1] and arr[mid] > arr[mid+1]: hi = mid-1
            else: lo = mid +1
        