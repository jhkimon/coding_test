N = int(input())

dp = [[0] * N for _ in range(N)]
data = []

for _ in range(N):
    lst = list(map(int, input().split()))
    data.append(lst)

dp[0][0] = data[0][0]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + data[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + data[i][j]
        else:
            dp[i][j] = max(dp[i-1][j] + data[i][j], dp[i-1][j-1] + data[i][j])

print(max(dp[N-1]))  # 마지막 행에서 최대값을 출력