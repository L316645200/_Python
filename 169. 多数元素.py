# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 解1:Hash，即以下解法
# 解2:排序，先排序，因为众数占据了一半的数组，n/2 中间数即众数
# 解3:随机取下标，判断是否是众数(因为众数超过数据的一半，期望值还是比较可观的)
# 解4:分治，pass
# 解5:Boyer-Moore 投票算法  取count=0, candidate=None，遍历数组，当count=0时，记当前数组值为1，candidate为当前值，其他值为-1，遍历完成后candidate即众数
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for m in set(nums):
            if nums.count(m) > n / 2:
                return m


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        return [m for m in set(nums) if nums.count(m) > len(nums) / 2][0]

