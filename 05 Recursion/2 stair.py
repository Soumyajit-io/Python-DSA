# # You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def stairpath(n):
    if n==2:return 2
    if n==1: return 1
    return  stairpath(n-1)+stairpath(n-2)

print(stairpath(4))