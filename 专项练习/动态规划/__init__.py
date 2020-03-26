
m = 5
n = 5
dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
print(dp)
