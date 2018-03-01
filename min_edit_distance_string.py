t = int(input().strip())

for case in range(t):
    n, m = map(int, input().split())
    str1, str2 = input().split()
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    dp[0][0] = 0
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = j
                continue
            if j == 0:
                dp[i][j] = i
                continue
            if str1[i-1] != str2[j-1]:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            else:
                dp[i][j] = dp[i-1][j-1]
    print(dp[n][m])
