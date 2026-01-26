l = [1,2,3,4,5,5]
#      10   , 10 
pre = []
pre.append(l[0])
for i in range (1,len(l)):
   pre.append(l[i]+pre[i-1])
print(pre)
for i in range (1,len(pre)):
   if 2*pre[i] ==pre[len(pre)-1]:
      print("Index found at ",i)
      break