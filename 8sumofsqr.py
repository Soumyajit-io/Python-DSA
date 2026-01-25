# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
import math
class Solution(object):
    def isp(self,n):
        root = int(math.sqrt(n))
        return root*root==n

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        x =0
        y = c
        while x<=y:
            if (self.isp(x) and self.isp(y)):
                return True
            elif (not self.isp(y)):
                y=int(y**0.5)*int(y**0.5)
                x=c-y
            else:
                x=int(x**0.5+1)*int(x**0.5+1)
                y=c-x
        return False