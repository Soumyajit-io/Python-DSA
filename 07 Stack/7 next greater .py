l = [3,1,2,7,4,6,2,3]

# algo : POP ANS PUSH
n=len(l)
st=[]
nge=[0]*n
nge[n-1]=-1
st.append(l[n-1])
for i in range(n-2,-1,-1):
    # pop all the elemnts smaller then arr of i
    while(len(st)>0 and st[-1]<=l[i]): 
        st.pop()
    if len(st)==0: 
        nge[i] = -1
    else:
        nge[i]=st[-1]
    st.append(l[i])
print(nge)

# sc : O (n)
# tc : O(2n)