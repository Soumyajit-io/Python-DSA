def stairpath(n):
    if n==2:return [11,2]
    if n==1: return [1]
    return  [int('1'+str(x)) for x in stairpath(n-1)]+[int('2'+str(x)) for x in stairpath(n-2)]

    # return  stairpath(n-1)+stairpath(n-2)

print(stairpath(10))