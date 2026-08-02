a=[[1,2],[3,4]]
b=[[5,6],[7,8]]

def multiplyMatrices(self, a, b):
        # code here
        r1=len(a)
        c1=len(a[0])
        r2=len(b)
        c2=len(b[0])
        res=[[0]*c2 for _ in range(r1)]
        if c1 == r2 :
            for i in range(0,r1):
                for j in range(0,c2):
                    summ=0
                    for k in range(c1):
                        summ+=a[i][k]*b[k][j]
                    res[i][j]= summ
        else:
            return None
        return res

print(res)