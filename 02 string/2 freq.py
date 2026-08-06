def getMaxOccuringChar(s):
        # code here
        c =""
        count=0
        ss = sorted(s)
        n=len(s)
        for i in range(n):
            temp=1
            j=i+1
            while(j<n and ss[i]==ss[j] ):
                temp+=1
                j+=1
            if temp > count :
                count = temp    
                c=ss[i]
        return c

print(getMaxOccuringChar("aaabggaagg"))