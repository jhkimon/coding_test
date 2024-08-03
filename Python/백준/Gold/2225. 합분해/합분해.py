MOD = 1_000_000_000
def dp_decompose(N, K):
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0] = [1] * (K+1)

    for i in range(1,N+1):
        for j in range(1,K+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
    return dp[N][K]

N, K = tuple(map(int, input().split()))
print(dp_decompose(N,K))