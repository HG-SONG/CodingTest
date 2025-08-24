class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = ""
        if (dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0):
            sign = "+"
        else:
            sign = "-"

        absDivend = abs(dividend)
        absDivisor = abs(divisor)
        answer = 0

        while absDivend >= absDivisor :
            temp = absDivisor
            mul = 1
            while absDivend >= (temp << 1):
                temp <<= 1
                mul <<= 1
            absDivend -= temp
            answer += mul

        answer = int(sign + str(answer))
        if answer > 2**31 -1:
            return 2**31 -1
        elif answer < -2**31:
            return -2**31
        else:
            return answer


