class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = len(nums) - 1
        while index >= 0:
            if nums[index - 1] < nums[index]:
                index -= 1
                break
            index -= 1

        if index >= 0:
            j = len(nums) - 1
            while nums[index] >= nums[j]:
                j -= 1
            nums[index], nums[j] = nums[j], nums[index]

        nums[index + 1:] = reversed(nums[index + 1:])
