# find first occurrence
nums= [1,3,3,3,3,4,5,5,6,7,8,9,10]
nums= [1,9]
target = 9
lo = 0
hi = len(nums)-1
n=len(nums)

# if n==1:
#    print(0)
while lo<=hi:
   mid = lo+ (hi-lo)//2
   if nums[mid]==target :
      if mid-1<0 or nums[mid]!=nums[mid-1]:
         print(mid)
         break
      else: hi=mid-1
   elif nums[mid] <target:
      lo = mid +1
   else : hi = mid-1
