def display(st):
    if len(st)==0:
        return
    print(st[-1])
    x=st.pop()
    display(st)
    st.append(x)
l = [10,20,30,40,50]
display(l)
display(l)