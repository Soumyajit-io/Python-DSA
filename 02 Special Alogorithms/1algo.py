l= [1,2,3,4,5]
for i in range(1,len(l)): 
   l[i]+=l[i-1]
print(l)