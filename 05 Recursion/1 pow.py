def poww(x,n):
    if n==1 :return x
    ans = poww(x,n-1)
    if n%2==0:
        return ans*ans
    else:
        return ans*ans*x


print(poww(2,11))