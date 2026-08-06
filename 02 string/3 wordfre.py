# return the word which is ossuring most number of time
s="a b  s"
s= "   heloo     a a a a a  exam exam exam exam exam exam  this is    soumo. i am is under water ytkyyjktykt kltkt  ttt k k        "

n=len(s)

l =[]
i=0
while(i<n):
    str=""
    while(i<n and s[i]==" " ):
        i+=1
    while(i<n and s[i]!=" "):
        str+=s[i]
        i+=1
    if (str!=""):
        l.append(str)
l.sort()
nn=len(l)                                             
count=0
c=''
i=0
while(i<nn):
    temp=1
    j=i+1
    while(j<nn and l[i]==l[j] ):
        temp+=1
        j+=1
    if temp > count and temp!=1 :
        count = temp    
        c=l[i]
    i=j
    
print(c)
print(count)

# use dict for better optimization 