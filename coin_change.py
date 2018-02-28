t = int(input().strip())

for case in range(t):
    m = int(input().strip())
    change = list(map(int, input().split()))
    n = int(input().strip())
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    for i in range(m):
        for j in range(change[i], n + 1):
            dp[j] = dp[j] + dp[j - change[i]] % 1000000007
    print(dp[n])