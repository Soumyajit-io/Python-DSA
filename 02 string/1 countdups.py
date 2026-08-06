# abbcdeffghh
# count = 5
s="a"
s="abbcdeffghh"

count =0
n=len(s)
if n==1:
    count==0
else:
    for i in range(n):
        if i==0:
            if s[i]!=s[i+1]:
                count+=1
        elif i==n-1:
            if s[i]!=s[i-1]:
                count+=1
        else:
            if (s[i]!=s[i+1] and s[i]!=s[i-1]):
                count+=1
print(count)
    
