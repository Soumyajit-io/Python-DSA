mat=[[1, 2, 3, 10],
    [4, 5, 6, 11],
    [7, 8, 9, 12],
    [13, 14, 15, 16]]

class Solution:
    def matrixDiagonally(self, mat):
        r= len(mat)
        c= len(mat[0])
        res =[]
        i=0
        j=0
        count=0
        for k in range(c):
            i=0
            j=k
            temp=[]
            while(j>=0):
                temp.append(mat[i][j])
                i+=1
                j-=1
            if count%2==0:
                temp.reverse()
            res.extend(temp)
            count+=1
        
        for k in range(1,r):
            i=k
            j=c-1
            temp=[]
            while(j>=0 and i< r):
                temp.append(mat[i][j])
                i+=1
                j-=1
            if count%2==0:
                temp.reverse()
            res.extend(temp)
            count+=1
        
            
            
        return res