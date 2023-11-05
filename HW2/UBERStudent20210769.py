import sys
from datetime import datetime, date

inputFile = sys.argv[1]
outputFile = sys.argv[2]

def find_weekday(date):
    weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    dow = date.weekday()
    return weekday[dow]

dic = dict() # 
with open(inputFile, "rt") as f:
    for lines in f:
        key = lines[:lines.find(',')]
        value = list(lines[lines.find(',') + 1:-1].split(','))
        if key not in dic:
            dic[key] = []
            dic[key].append(value)
        else:
            dic[key].append(value)

# 월/일/년도를 요일로 변경  
result = ""
for k, v in dic.items():
    for data in v:
        month, day, year = data[0].split('/')
        dow = find_weekday(date(int(year), int(month), int(day)))
        vehicles, trips = data[1], data[2]
        data[0] = dow

totalDic = dict()
for k, v in dic.items():
    resultDic = dict()
    for data in v:
        if data[0] not in resultDic:
            value = [int(data[1]), int(data[2])]
            resultDic[data[0]] = value
        else:
            resultDic[data[0]][0] += int(data[1])
            resultDic[data[0]][1] += int(data[2])
            value = [resultDic[data[0]][0], resultDic[data[0]][1]]
            resultDic[data[0]] = value
    totalDic[k] = resultDic


result = ""
for k, v in totalDic.items():
    for k1, v1 in totalDic[k].items():
        result += k + "," + k1 + " " + str(v1[0]) + "," + str(v1[1]) + "\n"

with open(outputFile, "wt") as f:
    f.write(result)