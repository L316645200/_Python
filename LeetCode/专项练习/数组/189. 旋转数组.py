# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 示例 1:
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 说明:
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums)-k:] + nums[:len(nums) - k]
        # nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[::-1]
        k = k % len(nums)
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        num = [0] * l
        k = k % l
        for i in range(k):
            num[i] = nums[l - k + i]
        for i in range(l - k):
            num[i + k] = nums[i]


# 暴力法懒得写了
l = [1,2,3,4,5,6,7]
k = 3
s = Solution()
print(s.rotate(l, k))