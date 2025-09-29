import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = bisect.bisect_left(nums,target)
        return pos