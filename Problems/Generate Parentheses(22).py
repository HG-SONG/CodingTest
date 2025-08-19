class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dic = dict()
        dic[0] = [""]
        dic[1] = ["()"]
        dic[2] = ["(())", "()()"]
        if n < 3:
            return dic[n]

        for i in range(3, n + 1):
            values = set()
            for j in range(i):
                for left in dic[j]:
                    for right in dic[i - j - 1]:
                        new = "(" + left + ")" + right
                        values.add(new)

            dic[i] = list(values)

        return dic[n]
