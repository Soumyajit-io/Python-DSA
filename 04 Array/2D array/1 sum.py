def sumOfMatrix(self, mat: list[list[int]]) -> int:
        # code here
        summ =0
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                summ+=mat[i][j]
        return summ