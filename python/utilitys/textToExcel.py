#!/usr/local/bin/python3
# coding=utf-8
from openpyxl import Workbook

def convert(file, opration):
    print ""

def iterateLinew(strings,function):
    lineIndex = 1
    wb = Workbook()
    ws = wb.active
    for line in strings.splitlines():
        lineIndex += 1
        fieldIndex = 1
        for fied in line.rsplit():
            fieldIndex += 1
            function(lineIndex,fieldIndex,fied,ws)
    wb.save(r'''E:\PycharmProjects\codebase\result.xlsx''')

def operation(lineIndex,fieldIndex,field,ws):
    cell = ws.cell(row=lineIndex, column=fieldIndex)
    cell.value = field.strip(r'''"''').strip("\‘").strip("`")


if __name__ == '__main__':
    fo = open("E:\PycharmProjects\codebase\ppcloud_2017-08-03.txt", "r+")
    str = fo.read(30000)
    #print str
    iterateLinew(str,operation)