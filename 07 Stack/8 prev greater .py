l = [100,80,60,70,60,75,85]

# algo : POP ANS PUSH
n=len(l)
st=[]
nge=[0]*n
nge[0]=-1
st.append(l[0])
for i in range(1,n,1):
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