from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = list(permutations(nums,len(nums)))
        s = set()
        for item in perm:
            s.add(item)
        return list(s)