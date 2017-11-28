n = int(input())

dp = []

dp.append(0) # 0
dp.append(0) # 1
dp.append(1) # 2
dp.append(1) # 3

for i in range(4, n + 1):
    dp.append(dp[i - 1] + 1); # 1을 빼고 최소 연산의 개수 계산

    if(i % 2 == 0): # 2로 나눠진다면
        dp[i] = min(dp[i], dp[i // 2] + 1) # 비교
    if(i % 3 == 0): # 3으로 나눠진다면
        dp[i] = min(dp[i], dp[i // 3] + 1) # 비교

print(dp[n])