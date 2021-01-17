#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tao
import jsonpath

# 1 save s 存起来
#
# key
#
# jsp
#
# save(string,key,jsp)
#
# value=jsonpath.jsonpath(string,jsp)
#
# self.saves[key]=value
#
#
#
# repalce（）
#     替换
import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(path)