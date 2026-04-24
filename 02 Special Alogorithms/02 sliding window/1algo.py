# use in 
# 1. subarray , substrings, largest/ smalleest sum

# Find max sum of sub array of k
l = [7,1,2,5,8,4,9,3,6]
msum = 0
k=3 
idx = -1
for i in range(0,len(l)-k):
   sumele = 0
   for j in range(i,i+k):
      sumele+=l[j]
   if msum<sumele:
      msum =sumele
      idx = i 

# print(msum,idx)

# for i in range(idx,idx+k):
#    print(l[i])

# now we will make it better>>>

prevsum = sum(l[:k])

maxsum = prevsum

i ,j= 1, k
n = len(l)
maxidx = -1
while (j<n):
   prevsum = prevsum + l[j] - l[i-1]
   if maxsum<prevsum:
      maxsum = prevsum
      maxidx = i
   
   i+=1 
   j+=1
# t.c. = O(n-k+k)= O(n)
print(maxsum)
print(maxidx)
