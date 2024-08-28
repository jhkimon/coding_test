N = int(input())
dp = [0 for _ in range(31)]

dp[2] = 3
for i in range(3, 31):
    if i % 2 == 1:
        dp[i] = 0
    else:
        dp[i] = dp[i-2] * 3 + 2 * sum(dp[:i-3]) + 2
print(dp[N])