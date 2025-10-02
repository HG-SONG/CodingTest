# from collections import deque
# from collections import Counter

# class Solution:
#     def cal(strs):
#         counter = Counter(list(strs))
#         key = tuple(counter.items())
#         return frozenset(key)

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d = deque(strs)
#         visited = dict()
#         answer = list([])
#         index = 0
#         while d:
#             popee = d.popleft()
#             splited = Solution.cal(popee)
#             if splited in visited:
#                 ind = visited[splited]
#                 answer[ind].append(popee)
#             else:
#                 answer.append([popee])
#                 visited[splited] = index
#                 index += 1
#         return answer

from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))  # 정렬된 단어가 key
            groups[key].append(word)
        return list(groups.values())