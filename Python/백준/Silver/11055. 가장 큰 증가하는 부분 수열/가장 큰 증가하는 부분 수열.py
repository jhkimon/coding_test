N = int(input())
nums = list(map(int, input().split()))

# DP 설정
dp = [0 for _ in range(N)]

# 초기 값
dp[0] = nums[0]

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])
    dp[i] = max(dp[i], nums[i])

print(max(dp))
