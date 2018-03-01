t = int(input().strip())

for case in range(t):
    n, m = map(int, input().split())
    str1 = input().strip()
    str2 = input().strip()
    if n == 0 or m == 0:
        print(0)
        continue
    dp = [[0 for i in range(m + 1)] for j in range(n+1)]
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
                continue
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1] % 1000000007
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j-1]) % 1000000007
    print(dp[n][m])
