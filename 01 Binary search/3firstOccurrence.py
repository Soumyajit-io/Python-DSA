# find first occurrence
nums= [1,3,3,3,3,4,5,5,6,7,8,9,10]
target = 1
lo = 0
hi = len(nums)-1

while lo<=hi:
   mid = lo+ (hi-lo)//2
   if nums[mid]==target :
      if nums[mid]!=nums[mid-1]:
         print(mid)
         break
      else: hi=mid-1
   elif nums[mid] <target:
      lo = mid +1
   else : hi = mid-1
