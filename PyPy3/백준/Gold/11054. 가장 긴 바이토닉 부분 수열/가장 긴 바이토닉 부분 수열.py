def longest_dp(N, data):
    max_num = 0
    for idx in range(1, N+1):
        dp = [1 for _ in range(N)]
        for i in range(idx):
            for j in range(i):
                if data[i] > data[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        dp_down = [1 for _ in range(N)]
        for i in range(N-1, idx-2, -1):
            for j in range(N-1, i-1, -1):
                if data[i] > data[j]:
                    dp_down[i] = max(dp_down[i], dp_down[j] + 1)
        max_num = max(max_num, max(dp) + max(dp_down) - 1)
    return max_num

N = int(input())
nums = list(map(int, input().split()))

print(longest_dp(N, nums))