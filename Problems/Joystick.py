def checkCharacter(char) -> int:
    stan = abs(ord(char) - 65)
    if stan > 13:
        interpor = stan - 13
        return 13 - interpor
    else:
        return stan

def encounterA(name) -> [int]:
    index = 0
    arrA = []
    for c in name:
        if c == 'A':
            arrA.append(index)
        index += 1
    return arrA

def back(name,index) -> str:
    reversedName = name[index+1:index:-1]
    result = name[:index] + reversedName
    return result

def solution(name):
    answer = 0
    aIndexArr = encounterA(name)
    count = 0
    for c in name:
        count += checkCharacter(c)
        count += 1

    answer = count - 1

    for index in aIndexArr:
        newCount = 0
        backedName = back(name,index)
        for c in backedName:
            newCount += checkCharacter(c)
            newCount += 1
        newCount -= 1
        newCount + index
        answer = min(answer, newCount)

    return answer

print(solution('JAN'))