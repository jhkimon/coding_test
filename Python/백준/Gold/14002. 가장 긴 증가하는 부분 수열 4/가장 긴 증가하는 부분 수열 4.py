def longest_dp(N, data):
    dp = [1 for _ in range(N)]
    
    for i in range(1, N):
        for j in range(i): # 이전까지의 값 확인
            if data[i] > data[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def dp_to_seq(N, nums, dp):
    count = max(dp); result = []
    for idx in range(len(dp)-1,-1,-1):
        if dp[idx] == count:
            result.append(nums[idx])
            count -= 1
    return ' '.join(map(str, result[::-1]))

N = int(input())
nums = list(map(int, input().split()))

dp = longest_dp(N, nums)
print(max(dp))
print(dp_to_seq(N, nums, dp))