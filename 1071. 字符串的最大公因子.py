# 对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
# 返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
#
# 示例 1：
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
# 示例 2：
# 输入：str1 = "ABABAB", str2 = "ABAB"
# 输出："AB"
# 示例 3：
# 输入：str1 = "LEET", str2 = "CODE"
# 输出：""
#
# 提示：
# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] 和 str2[i] 为大写英文字母

# 解1 字符串长度/当前长度 * 当前切片 == 目标字符串
# 解2 设s为两个字符串长度的最大公约数
# 解3 str1+str2 == str2+str1时，取最大公约数的切片即可，否则返回""
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        mi = min(m, n)
        for i in range(mi, 0, -1):
            if m % i == 0 and n % i == 0:
                if str1[0:i] * (m // i) == str1 and str1[0:i] * (n // i) == str2:
                    return str1[0:i]
        return ""


class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate_len = math.gcd(len(str1), len(str2))

        if str1[0:candidate_len] * (len(str1) // candidate_len) == str1 and str1[0:candidate_len] * (len(str2) // candidate_len) == str2:
            return str1[0:candidate_len]
        return ""


class Solution3:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate_len = math.gcd(len(str1), len(str2))

        if str1 + str2 == str2 + str1:
            return str1[0: candidate_len]
        return ""

str1 = "ABCABC"
str2 = "ABC"

s = Solution()
print(s.gcdOfStrings(str1, str2))
