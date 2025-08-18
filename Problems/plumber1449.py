def main():
    numberOfHole , tapeLength = map(int,input().split())
    holes = sorted(list(map(int,input().split())))
    print(calMin(holes, numberOfHole, tapeLength))

def calMin(holes, numberOfHole, tapeLength):
    minCount = numberOfHole
    previous = 0
    remainTape = tapeLength - 1
    tapeCount = 0 
    for popee in holes :
        if previous == 0:
            previous = popee
            continue

        gap = popee - previous 
        remainTape = remainTape - gap
        if remainTape == 0: 
            tapeCount += 1 
            remainTape = tapeLength - 1 
            previous = 0
        elif remainTape < 0: 
            tapeCount += 1 
            remainTape = tapeLength - 1 
            previous = popee
        elif remainTape > 0: 
            previous = popee
            continue
    if previous != 0:
        tapeCount += 1
    minCount = min(minCount,tapeCount)
    return minCount
        
main()
    