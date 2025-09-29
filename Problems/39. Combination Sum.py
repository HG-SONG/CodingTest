class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(start, path, total):
            if total == target:
                answer.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                dfs(i, path + [candidates[i]], total + candidates[i])

        dfs(0, [], 0)
        return answer