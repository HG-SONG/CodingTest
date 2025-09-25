class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        answer = -1

        if haystack == needle:
            return 0

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return answer