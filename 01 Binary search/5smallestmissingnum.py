nums= [0,1,2,3,4,5,6,7]
#      0,1,2,3,4,5,6,7, 8  9 10 11
lo = 0
hi = len(nums)-1
res =-1
while lo<=hi:
   mid = lo+ (hi-lo)//2
   if nums[mid]== mid:
      lo= mid+1
   elif nums[mid] !=mid:
      res= mid
      hi = mid -1

print(res)