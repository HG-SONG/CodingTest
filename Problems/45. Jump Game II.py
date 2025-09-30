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

#    class Solution:
#        def jump(self, nums: List[int]) -> int:
#            jumps = 0  # 점프 횟수
#           end = 0  # 현재 점프로 도달 가능한 최대 인덱스
#            farthest = 0  # 다음 점프로 도달 가능한 최대 인덱스
#
#            for i in range(len(nums) - 1):  # 마지막 칸은 자동 도달하므로 안 봄
#                farthest = max(farthest, i + nums[i])  # 가장 멀리 갈 수 있는 곳 갱신
#
#                if i == end:  # 현재 점프 범위의 끝에 도달했다면
#                    jumps += 1  # 점프 횟수 증가
#                    end = farthest  # 다음 점프 범위를 갱신
#
#            return jumps
