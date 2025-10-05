class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr1 = intervals
        arr1.append(newInterval)
        arr2 = sorted(arr1,key=lambda x: x[0])
        start = arr2[0][0]
        end = arr2[0][1]
        answer = []

        for item in arr2:
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
