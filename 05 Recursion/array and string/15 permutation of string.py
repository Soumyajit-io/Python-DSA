def permutation(res,ori):
    if len(ori) == 0:
        print(res)
        return
    for i in range(len(ori)):
        ch = ori[i]
        left = ori[0:i]
        right= ori[i+1:]
        permutation(res+ch,left+right)
    

permutation("","abcd")