st=[]

st.append(10) #0
st.append(20) #1
st.append(30) #2
st.append(50) #3

# add a element at idx 1

helper = []
n = len(st)
idx = 1
for _ in range(n-idx):
    helper.append(st.pop())

st.append(99)
for _ in range(n-idx):
    st.append(helper.pop())

print(st)

