# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        if len(nums) < 3:
            return l
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = i + 1
            h = len(nums) - 1
            if nums[i] > 0 or nums[h] < 0:
                break

            while k < h:
                s = nums[k] + nums[h] + nums[i]
                if s > 0:
                    h -= 1
                    while k < h and nums[h] == nums[h + 1]:
                        h -= 1
                elif s < 0:
                    k += 1
                    while k < h and nums[k] == nums[k - 1]:
                        k += 1
                else:
                    l.append([nums[k], nums[h], nums[i]])
                    h -= 1
                    k += 1
                    while k < h and nums[h] == nums[h + 1]:
                        h -= 1
                    while k < h and nums[k] == nums[k - 1]:
                        k += 1
        return l


s = Solution()
