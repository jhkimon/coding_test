MAX_N = 1_000_000; MOD = 1_000_000_009 # 전역변수

# 초기세팅
dp = [0 for _ in range(MAX_N + 1)]
dp[1] = 1; dp[2] = 2; dp[3] = 4

# for문
for i in range(4, MAX_N + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD


T = int(input())
nums = [int(input()) for _ in range(T)]

for num in nums:
    print(dp[num])