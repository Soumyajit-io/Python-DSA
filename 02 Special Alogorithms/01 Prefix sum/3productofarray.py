# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
l = [1,2,3,4]
prep = [1]
p1=l[0]

for i in range (1,len(l)):
   prep.append(p1)
   p1*=l[i]

print(prep)
sufp=[1]*len(l)
p2=l[len(l)-1]
for i in range (len(l)-2,-1,-1):
   sufp[i]=p2
   p2*=l[i]
print(sufp)

ans=[]
for i in range(len(sufp)):
   ans.append(prep[i]*sufp[i])
print(ans)