def triangleNumber(num):
    return num*(num+1)/2

def sol(inputNumber):
    triangleNumbers = [ triangleNumber(i) for i in range(1,44) ]
    leng = len(triangleNumbers)

    for a in range(leng):
        for b in range(a,leng):
            for c in range(b,leng):
                if triangleNumbers[a] + triangleNumbers[b] + triangleNumbers[c] == inputNumber:
                    return 1
    return 0

count = int(input())
outp = []

for i in range(count):
    num = int(input())
    outp.append(sol(num))

for item in outp:
    print(item)
