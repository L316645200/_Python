from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, m in enumerate(nums):
            if dic.get(target - m) is not None:
                return [dic[target - m], i]
            dic[m] = i


s = Solution()

print(s.twoSum([2, 7, 11, 15, 13], 9))
