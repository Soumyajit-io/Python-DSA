# 


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        num = 0
        lo = 0 
        hi = len(arr)-1
        flag= False
        idx =-1
        res=[]
        if x>arr[len(arr)-1] :
            lo = len(arr)
            hi = len(arr)-1
        elif x<arr[0] :
            lo = 0
            hi = -1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if arr[mid]==x:
                flag=True
                idx = mid
                break
            elif arr[mid]>x: hi = mid-1
            else: lo = mid+1
        if flag:
            flag=False
            res.append(arr[idx])
            lo=idx+1
            hi=idx-1
            num+=1
        if flag == False:
            while(hi >= 0 and lo < len(arr) and num < k):
                if abs(arr[hi]-x)<abs(arr[lo]-x) or (abs(arr[hi]-x)==abs(arr[lo]-x) and arr[hi]<arr[lo]):
                    res.append(arr[hi])
                    hi-=1
                else :
                    res.append(arr[lo])
                    lo+=1
                num+=1

            if (hi<0 and num<k and lo<len(arr)):
                while(num<k):
                    res.append(arr[lo])
                    lo+=1
                    num+=1
            if (lo>=len(arr) and num<k and hi>=0):
                while(num<k):
                    res.append(arr[hi])
                    hi-=1
                    num+=1
            return sorted(res)