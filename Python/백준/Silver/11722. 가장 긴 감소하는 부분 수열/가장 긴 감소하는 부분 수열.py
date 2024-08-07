def longest_dp(N, data):
    dp = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if data[i] < data[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

N = int(input())
nums = list(map(int, input().split()))

print(longest_dp(N, nums))