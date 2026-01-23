nums= [1,4,9,10,56]
target = 10
lo = 0
hi= len(nums)-1
while (lo<=hi):
   mid = lo + (hi-lo)//2
   if nums[mid] == target: 
      print(nums[mid])
      break
   elif nums[mid]>target: hi = mid-1
   else: lo = mid+1

# after lops ends lo ---> higher bound
#                 hi ---> lower bound 