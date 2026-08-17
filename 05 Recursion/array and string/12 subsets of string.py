def subsets(res , strr):
    if strr=="":
        print(res)
        return
    subsets(res+strr[0],strr[1:])
    subsets(res,strr[1:])


print(subsets("" , "abc"))