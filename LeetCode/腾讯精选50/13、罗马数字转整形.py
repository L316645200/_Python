class Solution:
    def romanToInt(self, s: str) -> int:
        roma_nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        num = 0
        for i in range(len(s) - 1):
            if roma_nums[s[i]] >= roma_nums[s[i + 1]]:
                num += roma_nums[s[i]]
            else:
                num -= roma_nums[s[i]]
        last_num = s[len(s) - 1]
        num = num + roma_nums[last_num]
        return num


s = Solution()
print(s.romanToInt('III'))
print(s.romanToInt('IV'))


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
             'CM': 800, 'M': 1000}
        sum = 0
        for i, n in enumerate(s):
            sum += d.get(s[max(i - 1, 0):i + 1], d[n])
        return sum


