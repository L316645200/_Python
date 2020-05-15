# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

# 思路：先排序，（可以去判断前三数和是否大于target和后三数和是否小于target，若是，直接返回和，极限情况，此步可不做），
# 遍历nums，判断ans和_sum与target的差值

# 复杂度， 时间，排序o(nlog n),双指针o(n²)， 总o(n²)
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[0:3])
        if ans > target:
            return ans
        elif sum(nums[-3:]) < target:
            return sum(nums[-3:])
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while right > left:
                _sum = nums[i] + nums[left] + nums[right]
                if abs(_sum - target) < abs(ans-target):
                    ans = _sum
                if _sum > target:
                    right -= 1
                elif _sum < target:
                    left += 1
                else:
                    return _sum
        return ans


nums = [-1, 2, 1, -4]
target = 1
solution = Solution()
print(solution.threeSumClosest(nums, target))