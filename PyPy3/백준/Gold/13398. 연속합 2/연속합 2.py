def consecutive_dp(N, data):
    dp0 = [0 for _ in range(N)]
    dp1 = [0 for _ in range(N)]
    dp0[0] = data[0]; dp1[0] = data[0]

    for i in range(1, N):
        dp0[i] = max(data[i], dp0[i-1] + data[i])
        dp1[i] = max(dp0[i-1], dp1[i-1] + data[i])

    return max(max(dp0), max(dp1))

N = int(input())
data = list(map(int, input().split()))

print(consecutive_dp(N, data))