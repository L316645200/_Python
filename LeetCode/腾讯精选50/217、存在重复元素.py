# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: true
# 示例 2:
#
# 输入: [1,2,3,4]
# 输出: false
# 示例 3:
#
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            nums.remove(num)
            if num in nums:
                return True
        else:
            return False


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = set(nums)
        if len(nums) == len(nums2):
            return False
        else:
            return True
        # return len(set(nums)) != len(nums)


class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = 0
        else:
            return False


class Solution4:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for s in range(len(nums) - 1):
            if nums[s] == nums[s + 1]:
                return True
        else:
            return False
