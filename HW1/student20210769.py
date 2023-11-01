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
    ws.cell(row = row, column = 7, value = total)

# list에 total 값 넣음
for row in range(2, ws.max_row + 1):
        list.append(ws.cell(row = row, column = 7).value)

rank = [sorted(list, reverse=True).index(i) + 1 for i in list]

# A, B, C 최대 몇 명 받을 수 있는지 계산
maxA = math.trunc((ws.max_row - 1) * 0.3)
maxB = math.trunc((ws.max_row - 1) * 0.7)

i = 0
grade = ''
for row in range(2, ws.max_row + 1):
    if (rank[i] <= maxA / 2):
        grade = 'A+'
    elif (rank[i] <= maxA):
        grade = 'A0'
    elif (rank[i] <= (ws.max_row - 1) * 0.5):
        grade = 'B+'
    elif (rank[i] <= maxB):
        grade = 'B0'
    elif (rank[i] < (ws.max_row - 1) / 0.85):
        grade = 'C+'
    elif (rank[i] < (ws.max_row + 1)):
        grade = 'C0'
    if (attendance == 0 or (ws.cell(row = row, column = 7).value) < 40):
        grade = 'F'
    i += 1
    ws.cell(row = row, column = 8, value = grade)

wb.save(filename = 'student.xlsx')
