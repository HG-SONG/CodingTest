from collections import deque

def solution(people, limit):
    answer = 0
    arr = deque()
    people.sort()
    for item in people:
        arr.append(item)

    boat = []

    while arr:
        remained = limit - sum(boat)
        if len(boat) == 0:
            maxman = arr.pop()
            boat.append(maxman)
        elif len(boat) == 1:
            minman = arr[0]
            if minman > remained:
                answer += 1
                boat.clear()
            else:
                arr.popleft()
                answer += 1
                boat.clear()
    if boat:
        return answer + 1
    else:
        return answer


