class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n-1
        top = 0
        bottom = n-1
        mat = [[0] * n for i in range(n)]
        answer = []
        count = 1

        while left <= right or top <= bottom :
            # 왼 -> 오
            for col in range(left,right+1):
                mat[top][col] = count
                count += 1
            top += 1

            # 위 -> 아래
            for row in range(top,bottom+1):
                mat[row][right] = count
                count += 1
            right -= 1

            # 오 -> 왼
            for col in range(right,left-1,-1):
                mat[bottom][col] = count
                count += 1
            bottom -= 1

            # 아래 -> 위
            for row in range(bottom,top-1,-1):
                mat[row][left] = count
                count += 1
            left += 1

        return mat