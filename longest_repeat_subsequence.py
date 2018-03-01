t = int(input().strip())
for case in range(t):
    str1 = input().strip()
    n = len(str1)
    dp = [[0 for i in range(n + 1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][i] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str1[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1] % 1000000007
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j-1]) % 1000000007
    print(dp[n][n])
