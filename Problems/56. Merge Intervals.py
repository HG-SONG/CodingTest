class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = sorted(intervals,key=lambda x: x[0])
        start = arr[0][0]
        end = arr[0][1]
        answer = []

        for item in arr:
            left = item[0]
            right = item[1]
            ## start ~ end 내부
            if start <= left and right <= end:
                continue
            ## start ~ end 에 걸쳐
            elif start <= left and left <= end and right > end:
                end = right
            ## start ~ end 외부
            else:
                answer.append([start,end])
                start = left
                end = right
        answer.append([start,end])
        return answer

