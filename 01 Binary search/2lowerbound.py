# find lower bound of target in a sorted array

nums= [1,3,5,6,8,9,13,19]
target = 10
lo = 0
hi = len(nums)-1
flag = False
while lo<=hi:
   mid = lo+ (hi-lo)//2
   if nums[mid]==target :
      print("found")
      flag = True
   elif nums[mid] <target:
      lo = mid +1
   else : hi = mid-1
if flag==False : print(nums[hi]) 



