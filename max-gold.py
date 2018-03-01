def max_gold_count(arr, n, m):
    dp= [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        dp[i][0] = arr[i][0]
    for j in range(1, m):
        for i in range(0, n):
            dp[i][j] = max(dp[i][j], dp[i][j-1])
            if i >= 1:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1])
            if i + 1 < n:
                dp[i][j] = max(dp[i][j], dp[i+1][j-1]) + arr[i][j]

    max_gold = 0
    for i in range(n):
        max_gold = max(max_gold, dp[i][m-1])
    print(str(max_gold))

gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]
max_gold_count(gold, 4, 4)
