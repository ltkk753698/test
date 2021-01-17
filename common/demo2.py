#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tao
import json
import re

import jsonpath

from common.functions import *
class people:
    url_common="litao"
    age="14"
    weight="65"






# data='{"name":"#name#","age":"#age#","weight":"#weight#"}'
#
# rex=r'#(.*?)#'
# def repalce(string,rex):
#
#     while re.search(rex,string):
#
#         tem=re.search(rex,string).group(1)
#
#         string=re.sub(rex,getattr(people(),tem),string,1)
#
#
#     return string
#
# c=repalce(data,rex)
#
# print(c)
saves={}
source={ "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}


jsp="$..price"
key="daiqain"
def save( source, key, jsp):
    value = jsonpath.jsonpath(source, jsp)[0]
    saves[key] = value

a=save(source,key,jsp)
print(saves)





