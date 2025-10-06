class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimed = s.split()
        popee = trimed.pop()
        return len(popee)