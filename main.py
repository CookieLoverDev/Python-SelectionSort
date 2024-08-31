import random

lst = random.sample(range(0, 50), 25)
print(lst)

startPoint = 0

while startPoint < len(lst):
    temp = lst[startPoint]
    tempIndex = startPoint
    for i in range(startPoint, len(lst)):
        if temp > lst[i]:
            temp = lst[i]
            tempIndex = i
    lst[startPoint], lst[tempIndex] = temp, lst[startPoint]
    startPoint += 1

print(lst)