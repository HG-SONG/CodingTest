class Solution:
    def jump(self, nums: List[int]) -> int:
        answer = float("inf")

        def dfs(start, count):
            nonlocal answer
            if count >= answer:
                return

            if start == len(nums) - 1:
                answer = min(count, answer)
                return

            if start > len(nums) - 1:
                return

            size = nums[start]

            for j in range(size, 0, -1):
                dfs(start + j, count + 1)
                prev = j

        dfs(0, 0)

        return answer
