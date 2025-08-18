num = int(input())
matrixArr = []
maxCount = 1  

def solve(matrixArr):
    global maxCount 
    for i in range(num):
        count = 1
        for j in range(1, num):
            if matrixArr[i][j] == matrixArr[i][j-1]:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 1
        maxCount = max(maxCount, count) 

    for j in range(num):
        count = 1
        for i in range(1, num):
            if matrixArr[i][j] == matrixArr[i-1][j]:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 1
        maxCount = max(maxCount, count)  

def pick(matrixArr):
    global maxCount 

    for i in range(num):
        for j in range(num - 1):
            if matrixArr[i][j] != matrixArr[i][j + 1]:
                matrixArr[i][j], matrixArr[i][j + 1] = matrixArr[i][j + 1], matrixArr[i][j]
                solve(matrixArr)
                matrixArr[i][j], matrixArr[i][j + 1] = matrixArr[i][j + 1], matrixArr[i][j]
    
    for i in range(num - 1):
        for j in range(num):
            if matrixArr[i][j] != matrixArr[i + 1][j]:
                matrixArr[i][j], matrixArr[i + 1][j] = matrixArr[i + 1][j], matrixArr[i][j]
                solve(matrixArr)
                matrixArr[i][j], matrixArr[i + 1][j] = matrixArr[i + 1][j], matrixArr[i][j]

for _ in range(num):
    row = list(input())
    matrixArr.append(row)

solve(matrixArr)
pick(matrixArr)
print(maxCount)