def maze(r,c):
    if r==2 and c==2:
        return ["DR","RD"]
    if r==1 and c==1:
        return []
    if r==1:
        return ["R"*(c-1)]
    if c==1:
        return ["D"*(r-1)]
    if r==0 or c==0:
        return []
    return ["D"+x for x in maze(r-1,c)]+["R"+x for x in maze(r,c-1)]

print(maze(3,3))