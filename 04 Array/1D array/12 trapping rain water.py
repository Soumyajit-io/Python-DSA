
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        # previous greatest elements
        prev=[0]*n
        maxx = height[0]
        prev[0]=-1
        for i in range(1,n):
            prev[i]=maxx
            if (height[i]>maxx):
                maxx=height[i]
        # next greatest elements
        nxt=[0]*n
        maxx = height[n-1]
        nxt[n-1]=-1
        for i in range(n-2,-1,-1):
            nxt[i]=maxx
            if (height[i]>maxx):
                maxx=height[i]
        # minimum array
        mini=[0]*n
        for i in range(0,n):
            mini[i]=min(prev[i],nxt[i])
        
        # cal water
        water =0
        for i in range(1,n-1,1):
            if(height[i]<mini[i]):
                water +=(mini[i]-height[i])
        return water