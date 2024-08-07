MAX_NUM = 10
dp = [0 for _ in range(MAX_NUM + 1)]
dp[1] = 1; dp[2] = 2; dp[3] = 4

for i in range(4, MAX_NUM+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


T = int(input())
nums = [int(input()) for _ in range(T)]
for num in nums:
    print(dp[num])