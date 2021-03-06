# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:
#
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
from functools import reduce
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(_) for _ in str(int(reduce(lambda x, y: str(x) + str(y), digits)) + 1)]


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        while True:
            if digits[n]==9 and n==0:
                digits[n] = 0
                digits.insert(0,1)
                break
            elif digits[n]==9:
                digits[n]=0
                n-=1
            else:
                digits[n] += 1
                break
        return digits

digits = [1]

s = Solution()
