l = [100,80,60,81,70,60,75,85]

# algo : POP ANS PUSH
n=len(l)
st=[]
nge=[0]*n
nge[0]=1
st.append(0)
for i in range(1,n,1):
    print(st[-1])
    while(len(st)>0 and l[st[-1]]<=l[i]):
        st.pop()
    if len(st)==0: 
        nge[i] = -1
    else:
        nge[i]= i- st[-1]
    st.append(i)

print(nge)
