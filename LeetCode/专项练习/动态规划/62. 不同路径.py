# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
# 示例 1:
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 示例 2:
# 输入: m = 7, n = 3
# 输出: 28
# 提示：
# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 10 ^ 9

# 递归，超时
class _Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        else:
            solution = Solution()
            return solution.uniquePaths(m, n - 1) + solution.uniquePaths(m - 1, n)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0 for _ in range(n)] for _ in range(m)]  # [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    table[i][j] = 1
                else:
                    table[i][j] = table[i-1][j] + table[i][j-1]
                    print(table)
        print(table)
        return table[m-1][n-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j-1]
                print(cur)
            pre = cur[:]
            print(pre)
        return pre[-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
                print(cur)
        return cur[-1]

m = 5
n = 5
sol = Solution()
print(sol.uniquePaths(m, n))
