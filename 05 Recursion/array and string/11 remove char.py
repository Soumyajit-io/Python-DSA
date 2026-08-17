def removechar(res , strr):
    if strr=="":
        return res
    if strr[0]!='a':
        return removechar(res+strr[0],strr[1:])
    else:
        return removechar(res,strr[1:])



print(removechar("" , "aahhh! ah"))