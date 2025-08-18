
# ------------------------------------------------
# 📌 1. 인트 <-> 스트링

s = "123"
lst = [int(c) for c in s]            # [1,2,3]

lst = [1, 2, 3]
s = ''.join(str(num) for num in lst) # "123"

# ------------------------------------------------
# 📌 2. 리스트 조작

arr1 = [0] * 10                             # 1차원 리스트 초기화
matrix = [[0] * 4 for _ in range(3)]        # 2차원 리스트 초기화

arr2 = [1, 2, 3, 4, 5]
arr2.pop(0)                                 # 첫 원소 제거 (O(n))
arr2.reverse()                              # 뒤집기 (제자리)
rev_arr = arr2[::-1]                        # 뒤집기 (새 리스트)

arr3 = [5, 2, 9, 1, 3]
arr3.sort()                                 # 오름차순 (제자리)
arr3.sort(reverse=True)                     # 내림차순 (제자리)
sorted_arr = sorted(arr3)                   # 새로운 리스트로 정렬
max_val = max(arr3)
min_val = min(arr3)
total = sum(arr3)

# ------------------------------------------------
# 📌 3. 문자열 조작

from collections import Counter

s1 = "hello"
rev_s1 = s1[::-1]
char_count = Counter("banana")              # 문자 개수
has_a = 'a' in s1
lower_s = s1.lower()
upper_s = s1.upper()

# ------------------------------------------------
# 📌 4. 순열과 조합

from itertools import permutations, combinations

arr4 = [1, 2, 3]
perm = list(permutations(arr4, 2))          # 순열
comb = list(combinations(arr4, 2))          # 조합

# ------------------------------------------------
# 📌 5. 스택 & 큐

from collections import deque

stack = []
stack.append(1)
stack.pop()                                 # LIFO

queue = deque()
queue.append(1)
queue.popleft()                             # FIFO

# ------------------------------------------------
# 📌 6. 우선순위 큐 (힙)

import heapq

min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 2)
min_val = heapq.heappop(min_heap)            # 최소값 꺼내기

max_heap = []
heapq.heappush(max_heap, -3)
max_val = -heapq.heappop(max_heap)           # 최대값 꺼내기

# ------------------------------------------------
# 📌 7. 딕셔너리 & defaultdict

from collections import defaultdict

dic = {"apple": 3, "banana": 5}
dic_default = defaultdict(int)
dic_default["apple"] += 1
val = dic.get("apple", 0) # 기본값 반환

# ------------------------------------------------
# 📌 8. 이진 탐색

import bisect

arr5 = [1, 3, 5, 7, 9]
pos = bisect.bisect_left(arr5, 4)            # 삽입 위치 (2)
bisect.insort(arr5, 4)                       # 자동 정렬 삽입
index = bisect.bisect_left(arr5, 6)

# ------------------------------------------------
# 📌 9. DFS & BFS

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start]:
        if nxt not in visited:
            dfs(graph, nxt, visited)
    return visited

def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return visited

# ------------------------------------------------
# 📌 10. 다익스트라

def dijkstra(graph, start):
    INF = float('inf')
    dist = {node: INF for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        if cur_dist > dist[cur_node]:
            continue
        for nxt, weight in graph[cur_node]:
            new_dist = cur_dist + weight
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))
    return dist

# ------------------------------------------------
# 📌 11. 이진 트리

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.value)

# ------------------------------------------------
# 📌 12. 람다 & 정렬

arr = [[3, 5], [1, 2], [2, 4]]
arr_sorted = sorted(arr, key=lambda x: x[1])

# ------------------------------------------------
# 📌 13. 필터링

arr = [1, 2, 3, 4, 6, 98, 5, 51]
filtered_arr = [x for x in arr if x >= 50]
filtered_arr2 = list(filter(lambda x: x >= 50, arr))

# ------------------------------------------------
# 📌 14. 시간 변환 (분 → 시:분)

def convert_to_time(m):
    return f"{m // 60:02d}:{m % 60:02d}"

# ------------------------------------------------
# 📌 15. Counter 정렬

nums = [1, 1, 2, 3, 3]
sorted_counter = sorted(Counter(nums).items(), key=lambda x: x[1])

# ------------------------------------------------
# 📌 16. 2D 리스트 컴프리헨션 예시

n, m = 3, 4
arr = [[i + j for j in range(m)] for i in range(n)]

# ------------------------------------------------
# 📌 17. 문자열로 연결된 가장 큰 수

from functools import cmp_to_key

def compare(x, y):
    return -1 if x + y > y + x else 1

str_numbers = ["1", "5", "3", "4", "62", "3", "6"]
sorted_numbers = sorted(str_numbers, key=cmp_to_key(compare))

# ------------------------------------------------
# 📌 18. 투포인터

def two_pointer(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            print(arr[left], arr[right])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1

# ------------------------------------------------
# 📌 19. 아스키코드

ch = 'A'
ascii_code = ord(ch)  # 65
char_val = chr(ascii_code) # 'A'

# ------------------------------------------------
# 📌 20. 백트래킹 (섬 개수 예시)

def backtracking(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    def dfs(x, y):
        if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != '1':
            return
        grid[x][y] = '#'
        for dx, dy in directions:
            dfs(x + dx, y + dy)
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    return count
