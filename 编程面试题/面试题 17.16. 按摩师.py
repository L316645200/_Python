# 一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。
# 在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。
# 给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。
# # 注意：本题相对原题稍作改动（不知原题是何题）
# # 示例 1：
# # 输入： [1,2,3,1]
# # 输出： 4
# # 解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
# # 示例 2：
# # 输入： [2,7,9,3,1]
# # 输出： 12
# # 解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
# # 示例 3：
# # 输入： [2,1,4,5,3,1,1,3]
# # 输出： 12
# # 解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        dp0, dp1 = 0, 0
        for num in nums:
            tdp0 = max(dp0, dp1)  # 第i号预约不接的最大时长
            tdp1 = dp0 + num  # 第i号预约接的最大时长
            dp0, dp1 = tdp0, tdp1
            # dp0, dp1 = max(dp0, dp1), dp0 + num
            print(num, dp0, dp1)
        return max(dp0, dp1)


l = [2,1,4,5,3,1,1,3]
s = Solution()
print(s.massage(l))

class _Solution:
    def massage(self, nums: List[int]) -> int:
        dp0, dp1 = 0, 0
        for num in nums:
            dp0, dp1 = dp1, max(dp0+num, dp1)
            print(num, dp0, dp1)
        return max(dp0, dp1)

s = _Solution()
print(s.massage(l))
