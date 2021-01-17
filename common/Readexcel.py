#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tao
import os
import xlrd



class readexcel:

    def __init__(self,filename,number):

        self.filename=filename

        self.number=number

    def Read(self):

        # 获取当前项目路径
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #拼接当前路径

        data_path = os.path.join(path, self.filename)
        # 读取excel
        excel = xlrd.open_workbook(data_path)

        # 读取指的的sheet

        sheet = excel.sheet_by_index(self.number)

        # 获取sheet行数

        nrows = sheet.nrows

        # 获取sheet列数

        ncols = sheet.ncols

        # 获取表头

        key = []

        for i in range(ncols):
            key.append(sheet.cell(0, i).value)

        # 获取所有数据

        list = []

        for i in range(1, nrows):
            temp = {}

            for j in range(ncols):
                temp[key[j]] = sheet.cell(i, j).value

            list.append(temp)

        return list


if __name__ == '__main__':
    op=readexcel('data/testcase.xlsx',1)

    li=   op.Read()
    print(li)
    a=[]
    for i in li:
        a.append(i['method'])

    print(a)
