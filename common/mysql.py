#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tao
import pymysql
from pymysql.cursors import DictCursor
#建立链接


conn=pymysql.connect(host='120.78.128.25',port=3306,
                     user='future',password='123456',
                     charset='utf8',database='futureloan',cursorclass=DictCursor)

#游标
cursor = conn.cursor()

#发起请求 执sql语句
mobile=13212332111
cursor.execute('select * from member where mobile_phone = %s;',args=[mobile])

#获取游标结果

one=cursor.fetchall()
print(one)
cursor.close()

conn.close()

