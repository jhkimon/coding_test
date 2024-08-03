MOD = 9901

def zoo_dp(N):
    dp0 = [0 for _ in range(N+1)]
    dp1 = [0 for _ in range(N+1)]
    dp2 = [0 for _ in range(N+1)]

    dp0[1] = 1; dp1[1] = 1; dp2[1] = 1

    for i in range(2, N+1):
        dp0[i] = (dp0[i-1] + dp1[i-1] + dp2[i-1]) % MOD
        dp1[i] = (dp0[i-1] + dp2[i-1]) % MOD
        dp2[i] = (dp0[i-1] + dp1[i-1]) % MOD
    return (dp0[N] + dp1[N] + dp2[N]) % MOD

N = int(input())
print(zoo_dp(N))