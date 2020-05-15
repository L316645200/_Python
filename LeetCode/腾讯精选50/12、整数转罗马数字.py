class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        nums = {1000: 'M', 500: 'D', 400: 'CD', 100: 'C', 50: 'L', 40: 'XL', 10: 'X', 5: 'V', 4: 'IV', 1: 'I'}
        for key in sorted(nums.keys(), reverse=True):
            a = num // key
            if a == 0:
                continue
            res += nums[key] * a
            num -= a * key
            if num == 0:
                break
        return res


s = Solution()
print(s.intToRoman(2877))


