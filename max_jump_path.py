def max_jump_path(arr, n):
    dp = [0 for i in range(n)]
    dp[0] = arr[0]
    for i in range(1, n):
        max_j = 0
        dp[i] = arr[i]
        range_index = int((i+1)**(1/2)) + 1
        for j in range(1, range_index):
            if (i+1) % j == 0 and i+1 != j:
                if dp[j-1] > max_j:
                    max_j = dp[j-1]
                divisor = int((i+1)/j)
                if dp[divisor - 1] > max_j and j != 1:
                    max_j = dp[divisor - 1]
        dp[i] += max_j

    print(str(dp))

arr = [2, 3, 1, 4, 6, 5]
max_jump_path(arr, len(arr))
