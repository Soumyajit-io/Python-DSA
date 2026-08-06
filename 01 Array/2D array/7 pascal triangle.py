# Given an integer numRows, return the first numRows of Pascal's triangle.
# 1
# 11
# 121
# 1331
# 14641

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[[1],[1,1]]

        if numRows == 1 :
            return [[1]]
        elif(numRows==2):
            return res
        else:
            for i in range(1,numRows-1):
                l=[1]*(i+2)
                for j in range(1,i+1):
                    l[j]=res[i][j] + res[i][j-1]
                res.append(l)
            return res