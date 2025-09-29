from collections import deque

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        leftIndex = 0
        rightIndex = len(nums) - 1

        while leftIndex <= rightIndex:
            midIndex = (leftIndex + rightIndex) // 2

            leftV = nums[leftIndex]
            rightV = nums[rightIndex]
            midV = nums[midIndex]

            if leftV == target:
                return leftIndex
            elif midV == target:
                return midIndex
            elif rightV == target:
                return rightIndex

            if leftV < target and target < midV:
                # 왼쪽 연속구간
                rightIndex = midIndex - 1
            elif target < rightV and midV < target:
                # 오른쪽 연속구간
                leftIndex = midIndex + 1
            elif leftV > midV and target < midV:
                # 왼쪽에 회전기준있고, 중간보다 target이 작다? 무조건 왼쪽에 있음
                rightIndex = midIndex - 1
            elif leftV > midV and midV < target:
                # 왼쪽에 회전기준있고, 중간보다 target이 크다?
                if leftV < target:
                    # 근데 left보다도 target이 커? 무조건 왼쪽에있음
                    rightIndex = midIndex - 1
                else:
                    # 근데 left보다는 target이 작아? 무조건 오른쪽에 있음
                    leftIndex = midIndex + 1
            else:
                # 오른쪽에 회전기준있고, 중간보다 target 커? 무조건 오른쪽에 있음
                # 오른쪽에 회전기준있고, 중간보다 target이 작아? 무조건 오른쪽에 있음
                leftIndex = midIndex + 1

        return -1

# 내 풀이도 정답이긴 하고, 성능상 문제도 없지만,
# '중간을 기준으로, 어느쪽이 정렬되어 있는지? -> 왼쪽이 정렬되어 있다면, target이 거기에 속하는지? -> 속해? 그럼 왼쪽다시 탐색 , 안속해? 그럼 오른쪽 다시 탐색