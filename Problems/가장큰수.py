from functools import cmp_to_key

def compare(x, y):
    return 1 if int(x + y) > int(y + x) else -1

def solution(numbers):
    answer = ""
    arr = list(map(str, numbers))
    arr2 = sorted(arr, key=cmp_to_key(compare))

    while arr2:
        popee = arr2.pop()
        if popee == '0' and answer == '0':
            continue
        answer += popee

    return answer