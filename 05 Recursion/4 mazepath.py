def maze(r,c):
    if r==1 and c==1:
        return 1
    elif r==0 or c==0:
        return 0
    return maze(r-1,c)+maze(r,c-1)

print(maze(3,3))