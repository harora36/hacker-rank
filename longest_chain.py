class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def longest_chain(pairs):
    n = len(pairs)
    sorted_list = sorted(pairs, key = lambda x: (x.a))
    dp = [1 for i in range(n)]
    max_len = 1
    for i in range(1, n):
        for j in range(i):
            pair1 = sorted_list[j]
            pair2 = sorted_list[i]
            if pair1.b < pair2.a and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                if dp[i] > max_len:
                    max_len = dp[i]
    return max_len
arr = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]
print(longest_chain(arr))
