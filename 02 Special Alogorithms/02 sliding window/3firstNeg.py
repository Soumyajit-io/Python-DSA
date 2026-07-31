# first negative number in every window of size k
l= [2,3,4,4,-7,-1,4,-2,6]

k=2
res = []
i ,j = 1, k
n = len(l)
p =-1

for i in range(0,k) :
   if l[i]<0 :
      p = i
      break

if p==-1 :
   res.append(1)
else:
   res.append(l[p])


while (j<n):
   if p>=i:
      res.append(l[p]) 
   else:
      p = -1
      for x in range(i,j+1):
         if l[x]<0:
            p =x
            break
      if p!=-1:
         res.append(l[p])
      else:
         res.append(1)
   
   i+=1 
   j+=1
# t.c. = O(n-k+k)= O(n)
print(l)
print(res)