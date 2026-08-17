def prevSmaller(arr):
		# code here
        n=len(arr)
        st=[]
        nge=[0]*n
        nge[0]=-1
        st.append(arr[0])
        for i in range(1,n):
            while(len(st)>0 and st[-1]<=arr[i]): 
                st.pop()
            if len(st)==0: 
                nge[i] = -1
            else:
                nge[i]=st[-1]
            st.append(arr[i])
        return nge
prevSmaller([1, 6, 2])