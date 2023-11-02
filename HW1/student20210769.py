#!/usr/bin/python3

from openpyxl import load_workbook
import math

wb = load_workbook(filename = 'student.xlsx')
ws = wb['Sheet1']

list = []
for row in range(2, ws.max_row + 1):
    mid = ws.cell(row = row, column = 3).value
    final = ws.cell(row = row, column = 4).value
    hw = ws.cell(row = row, column = 5).value
    attendance = ws.cell(row = row, column = 6).value

    # total
    total  = mid * 0.3 + final * 0.35 + hw * 0.34 + attendance
    list.append(total) # list에 total 값 넣음
    ws.cell(row = row, column = 7, value = total)

# 순위
# sorted_score = sorted(score, reverse = True) 
# ranks = [sorted_score.index(s) + 1 for s in score]

rank = [sorted(list, reverse=True).index(i) + 1 for i in list]

#A, B, C 최대 몇 명 받을 수 있는지 계산
maxA = math.trunc((ws.max_row - 1) * 0.3)
maxB = math.trunc((ws.max_row - 1) * 0.7)

# 동점자 계산
stuNum = ws.max_row - 1 
maxNum_A = math.trunc(stuNum * 0.15) # 11등
maxNum_A0 = math.trunc(stuNum * 0.3) # 22등
maxNum_B = math.trunc(stuNum * 0.5) # 37등
maxNum_B0 = math.trunc(stuNum * 0.7) # 51등
maxNum_C = math.trunc(stuNum * 0.85) # 62등

i = 0
garde = ''
gradeList = []
for row in range(2, ws.max_row + 1):
    if ((rank[i] <= maxA / 2) and (rank.count(rank[i]) <= maxNum_A)):
        grade = 'A+'
    elif ((rank[i] <= maxA) and (rank.count(rank[i]) <= maxA)):
        grade = 'A0'
    elif ((rank[i] <= (ws.max_row - 1) * 0.5) and ((rank.count(rank[i]) <= maxNum_B - maxNum_A0))):
        grade = 'B+'
    elif (rank[i] <= maxB and (rank.count(rank[i]) <= maxB)):
        grade = 'B0'
    elif ((rank[i] < (ws.max_row - 1) * 0.85) and ((rank.count(rank[i]) <= maxNum_C - maxNum_B0))):
        grade = 'C+'
    else:
        grade = 'C0'
    if ((ws.cell(row = row, column = 6).value)== 0 or (ws.cell(row = row, column = 7).value) < 40):
        grade = 'F'
    ws.cell(row = row, column = 8, value = grade)
    gradeList.append(grade)
    i += 1

wb.save(filename = 'student.xlsx')
