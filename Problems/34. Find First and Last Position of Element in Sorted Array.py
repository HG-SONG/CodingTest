class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(target):
            answer = -1
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    answer = mid
            return answer

        def findRight(target):
            answer = -1
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    answer = mid
            return answer

        left = findLeft(target)
        right = findRight(target)
        return [left, right]