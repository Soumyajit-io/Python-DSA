# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

# Example 1:

# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

class Solution(object):
    def helperA(self,weights,days,c):
        res = [] 
        summ =0
        idx=0
        while len(res)<days:
            if summ<c and idx>=len(weights):
                res.append(summ)
                break
            if summ<c:
                summ+=weights[idx]
                idx+=1
            elif summ==c:
                res.append(summ)
                summ=0
            elif summ>c:
                summ-=weights[idx-1]
                res.append(summ)
                summ=0
                idx-=1
        return sum(res)==sum(weights)


    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        mixc=0
        lo = max(weights)
        hi = sum(weights)
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if self.helperA(weights, days,mid) :
                minc=mid
                hi=mid-1
            else:
                lo=mid+1
        return minc