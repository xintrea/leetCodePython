#!/bin/python3

# for i in range(10): print("first"); print("second")

a=lambda n: n+10
print( a(1) )

n=5
dp = [ ([False] * n) for _ in range(n) ]
ans = [0, 0]
       
for i in range(n):
    dp[i][i] = True
            
print( str(dp) )
            
