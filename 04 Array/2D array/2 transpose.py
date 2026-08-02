def transpose(self, matrix):

        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r=len(matrix)
        c=len(matrix[0])
        m = [[0] * r for _ in range(c)]
        for i in range(0,c):
            for j in range(0,r):
                    m[i][j]=matrix[j][i]
        return m