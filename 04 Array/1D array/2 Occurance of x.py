l=[4,66,9,78,23,66,4]
print(l)

idx = -1
x=66
for i in range(len(l)-1,-1,-1):
    if l[i]==x:
        idx=i
        break

print(idx)