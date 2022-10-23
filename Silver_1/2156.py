n = int(input())
wine = [int(input()) for i in range(n)]
dp = [0 for i in range(n+1)]
dp[1] = wine[0]
if n > 1:
    dp[2] = wine[0]+wine[1]
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-3]+wine[i-2]+wine[i-1], dp[i-2]+wine[i-1])
print(dp[n])
