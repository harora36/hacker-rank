class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "( " + str(self.x) + " , " + str(self.y) + " )"


def max_len_snake(element, n, m):
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = 0
    max_len = 0
    for i in range(n):
        for j in range(m):
            if i-1 >= 0 and abs(element[i][j] - element[i-1][j]) == 1:
                dp[i][j] = max(dp[i][j], 1 + dp[i-1][j])
            if j-1 >= 0 and abs(element[i][j] - element[i][j-1]) == 1:
                dp[i][j] = max(dp[i][j], 1 + dp[i][j-1])
            if dp[i][j] > max_len:
                max_len = dp[i][j]
                max_row = i
                max_col = j
    snake = []
    i = max_row
    j = max_col
    snake.append(Point(i, j))
    while max_len > 0:
        if i-1 >= 0 and dp[i][j] - 1 == dp[i-1][j]:
            i -= 1
        elif j-1 >= 0 and dp[i][j] - 1 == dp[i][j-1]:
            j -= 1
        snake.append(Point(i, j))
        max_len -= 1
    for point in reversed(snake):
        print(str(element[point.x][point.y]) + str(point))


mat = [[9, 6, 5, 2],
       [8, 7, 6, 5],
       [7, 3, 1, 6],
       [1, 1, 1, 7]]

max_len_snake(mat, 4, 4)
