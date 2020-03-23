# 时间复杂度O(m+n)log(m+n)(不符合)
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums = nums1 + nums2
#         nums.sort()
#         l = len(nums) - 1
#         if l % 2 == 0:
#             return nums[(l + 1) // 2]
#         else:
#             return (nums[l // 2] + nums[l // 2 + 1]) / 2
from typing import List


class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        if m > n:
            m, n, A, B = n, m, B, A
        if n == 0:
            raise ValueError
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2  # 1,3,5   1,2,4,5
            j = half_len - i
            # i,j为A，B的中位数, 当B左边的最大值大于A右边的最小值时,j应该减小或者i增大
            if i < m and B[j-1] > A[i]:
                imin += 1
            elif i > 0 and A[i-1] > B[j]:
                imax -= 1
            else:
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0



