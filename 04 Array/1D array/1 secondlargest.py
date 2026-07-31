l=[4,6,9,78,23,66,4]
print(l)
maxe=0
for i in l:
    if i>maxe:
        maxe = i
print(maxe)

smax =0
for i in l:
    if i>smax and i!= maxe:
        smax =i
print(smax)