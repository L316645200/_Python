# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
# 示例：
# 输入：A = [4,5,0,-2,-3,1], K = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 K = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
from typing import List


# class Solution:
#     def subarraysDivByK(self, A: List[int], K: int) -> int:
#         l = len(A)
#         count = 0
#         for i in range(l):
#             s = 0
#             for j in range(i, l):
#                 s += A[j]
#                 if s % K == 0:
#                     count += 1
#         return count
#
#


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        record = {0: 1}
        total, ans = 0, 0
        for elem in A:
            total += elem
            modulus = total % K
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1

        return ans
## 前缀和的思想，官方题解。。
## 好难.............................
A = [4, 1, 0, -2, -3, 1]
K = 5
s = Solution()
print(s.subarraysDivByK(A, K))


