def maze(r,c,s):
    if r==1 and c==1:
        print(s)
        return 1
    elif r==0 or c==0:
        return 0
    return maze(r-1,c,s+"D")+maze(r,c-1,s+"R")

print(maze(3,3,""))