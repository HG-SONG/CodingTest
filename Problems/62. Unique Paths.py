class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        r = min(m - 1, n - 1)

        num = 1
        den = 1
        for i in range(1, r + 1):
            num *= total - r + i
            den *= i
        return num // den
