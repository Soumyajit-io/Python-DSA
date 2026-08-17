# 1 2 3

# 1 2 
# 1 3
# 2 3
# 123
arr = [1 , 2 ,3 ,4]

for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        for k in range(i,j+1):
            print(arr[k], sep=' ',end=' ')
        print("\n")