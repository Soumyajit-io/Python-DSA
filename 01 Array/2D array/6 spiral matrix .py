# Given an m x n matrix, return all elements of the matrix in spiral order.
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]



class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        l=[]
        sc=0
        ec=len(matrix[0])-1
        sr=0
        er=len(matrix)-1
        
        while(sr<=er and sc<=ec):
            # right
            for i in range(sc,ec+1,1):
                l.append(matrix[sr][i])
                
            sr+=1

            # down
            for i in range(sr,er+1 ,1):
                l.append(matrix[i][ec])
                
            ec-=1



            if(sr>er or sc>ec):
                break
            # left
            for i in range(ec,sc-1 ,-1):
                l.append(matrix[er][i])
            er-=1
            
            
            # up
            for i in range(er,sr-1,-1):
                l.append(matrix[i][sc])

            sc+=1

        return l
        