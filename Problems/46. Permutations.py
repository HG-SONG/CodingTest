from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = list(permutations(nums,len(nums)))
        return perm