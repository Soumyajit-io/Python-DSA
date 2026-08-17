def toh(n,s,h,d): # s --> source,d-->dest,h-> helper
    if n==0: return 
    toh(n-1,s,d,h)
    print(s," -> ",d)
    toh(n-1,h,s,d)

toh(2,"A","B","c")