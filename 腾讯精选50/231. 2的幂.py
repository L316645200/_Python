class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 1
        while i < n:
            i *= 2
        else:
            if i == n:
                return True
            else:
                return False


class SimpleSolution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

print(2 ^ 1)
