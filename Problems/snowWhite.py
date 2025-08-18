row = 9
list = []
sum = 0 
target = []

for idx in range(row): 
    number = int(input())
    list.append(number)
    sum += number

minus = sum - 100 
for i in range(row):
    for j in range(i+1,row):
        if list[i] + list[j] == minus: 
            target.append(list[i])
            target.append(list[j])
            break

for item in list:
    if item == target[0] or item == target[1]:
        continue
    print(item)
