# 输入整数数组arr ，找出其中最小的k个数。
# 例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
# 示例1：
# 输入：arr = [3, 2, 1], k = 2
# 输出：[1, 2]
# 或者[2, 1]
# 示例2：
# 输入：arr = [0, 1, 2, 1], k = 1
# 输出：[0]
# 限制：
#
# 0 <= k <= arr.length <= 10000
# 0 <= arr[i] <= 10000
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]

# 直接排序后取前k个数可能不是题目要考的（虽然这是最简单的）

# 可能考的是快排思想

# 按照快排的思想，取出前k个值为l排序，遍历剩下的值与arr[k-1]比较，小于则继续往前比较直至可以插入，大于跳过
