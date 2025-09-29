class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = sorted(candidates)
        answer = []
        visited = set()

        def dfs(start, path, total):
            if total == target:
                if tuple(path) in visited:
                    return
                answer.append(path)
                visited.add(tuple(path))
                return

            if total > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                if arr[i] == prev:
                    continue
                prev = arr[i]

                dfs(i + 1, path + [arr[i]], total + arr[i])

        dfs(0, [], 0)
        return answer
