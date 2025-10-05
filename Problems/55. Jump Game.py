class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum = 0

        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        for index, step in enumerate(nums):
            if index > maximum:
                return False

            if index == len(nums) - 1:
                continue

            if step == 0:
                continue
            else:
                maximum = max(maximum, index + step)

            if maximum >= len(nums) - 1:
                return True

        return False

