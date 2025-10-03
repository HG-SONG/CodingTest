class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        answer = []

        while top <= bottom and left <= right:
            # 왼 -> 오
            for col in range(left, right + 1):
                item = matrix[top][col]
                answer.append(item)
            top += 1

            # 위 -> 아
            for row in range(top, bottom + 1):
                item = matrix[row][right]
                answer.append(item)
            right -= 1

            # 오 -> 왼
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    item = matrix[bottom][col]
                    answer.append(item)
                bottom -= 1

                # 아 -> 위
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    item = matrix[row][left]
                    answer.append(item)
                left += 1

        return answer


