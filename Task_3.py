import math
from frequency import binarySequence
from mpmath import gammainc

# Разбиваем массив на подмассивы из 8 элементов
dividedList = []
for i in range(0,16):
    dividedList.append(binarySequence[0+8*i:8+8*i])
print(dividedList)
#[[1, 1, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0, 1, 1], [1, 1, 0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0]]

# Ищем максимальную длину каждой подпоследовательности подряд идущих единиц:
maxOnesLength = []
for items in dividedList:
    count = 0
    maxCount = 0
    for item in items:
        if item == 1:
            count+=1
            if count>maxCount:
                maxCount=count
        else:
            count = 0
    maxOnesLength.append(maxCount)
print(maxOnesLength)
# [2, 2, 3, 5, 1, 8, 6, 3, 4, 2, 4, 3, 2, 3, 2, 3]

# Считаем статистику по разным длинам Vi:
vList = []
count = 0
for i in maxOnesLength:
    if i<=1:
        count+=1
vList.append(count)
count = 0
for i in maxOnesLength:
    if i == 2:
        count+=1
vList.append(count)
count=0
for i in maxOnesLength:
    if i == 3:
        count+=1
vList.append(count)
count=0
for i in maxOnesLength:
    if i>=4:
        count+=1
vList.append(count)
print(vList)
# [1, 5, 5, 5]

# Вычислим хи-квадрат:
xSquare = pow(vList[0]-16*0.2148, 2)/(16*0.2148)+pow(vList[1]-16*0.3672, 2)/(16*0.3672)+pow(vList[2]-16*0.2305, 2)/(16*0.2305)+pow(vList[3]-16*0.1875, 2)/(16*0.1875)
print(xSquare)
# 3.658217833426413

Pvalue = gammainc(1.5, xSquare/2)
print(Pvalue)
# 0.266589529280881 > 0.01 => последовательность прошла тест
