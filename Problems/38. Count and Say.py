from collections import deque

class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(n):
            if n == 1:
                return "1"
            else:
                answer = ""
                re = rle(n - 1)
                deq = deque(list(re))
                while deq:
                    count = 0
                    popee = deq.popleft()
                    count += 1

                    while deq and popee == deq[0]:
                        deq.popleft()
                        count += 1
                    s = str(count) + str(popee)
                    answer += s

                return answer

        return rle(n)