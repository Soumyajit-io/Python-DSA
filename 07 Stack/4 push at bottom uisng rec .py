def pushhh(st,v,i):
    if len(st)==i:
        st.append(v)
        return
    x=st.pop()
    pushhh(st,8,i)
    st.append(x)
l = [10,20,30,40,50]
i = 2
ele = 99
pushhh(l,ele,i)
print(l)
