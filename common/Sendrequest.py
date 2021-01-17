#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tao
import json
import re

import jsonpath


from common.functions import *
from common.Readexcel import readexcel
import requests

from common.logger import LoggerHandler


# Python的第三方库requests提示警告InsecureRequestWarning的问题
# requests.packages.urllib3.disable_warnings()
logger=LoggerHandler()

class SendRquest:

    #全局变量池
    saves={}
    #识别${}的正则表达式
    Reg=r"\$\{(.*?)\}"

    #识别函数助手
    Func_Reg=r'__(.*?)\(\)'



    def __init__(self):
        self.session=requests.session()

    def send_request(self,host,url,method,params=None,dict_header=None,data=None,dict_json=None,saves=None,code=None,expect=None,file=None):

        base_url=host+url


        base_url    =    self.repalce(base_url)
        dict_header = self.repalce(dict_header)
        dict_json   =  self.repalce(dict_json)

        if dict_header:
            dict_header = json.loads(dict_header)

        if dict_json:
            dict_json =json.loads(dict_json)

        res=self.session.request(method,base_url,params=params,headers=dict_header,data=data,json=dict_json)

        self.api_log(method,base_url,params=params,dict_header=dict_header,dict_json=dict_json,
                     code=res.status_code, res_text=res.text,res_header=res.headers)

        #保存saves 到全局变量池
        if saves:
            saves=saves.split(';')
            for save in saves:
                key=save.split('=')[0]

                jsp=save.split('=')[1]

                self.save(res.json(),key,jsp)
        try:
            return res

        except Exception as e:
            logger.error("接口请求异常,原因：{}".format(e))
            raise e

    #提取参数并保存至全局变量池
    def save(self,source,key,jsp):

        value=jsonpath.jsonpath(source,jsp)[0]

        self.saves[key] = value
        logger.info("保存 {}=>{} 到全局变量池".format(key, value))

     #替换含有正则的字符串
    def repalce(self,string):

        while re.search(self.Reg,string):
            #取出正则表达式的

            key=re.search(self.Reg,string).group(1)

            string=re.sub(self.Reg,str(self.saves[key]),string,1)

        while re.search(self.Func_Reg, string):
            # 取出正则表达式的

            key = re.search(self.Func_Reg, string).group(1) + "()"
            value = eval(key)
            string = re.sub(self.Func_Reg, value, string, 1)

        return string


    def api_log(self,method,url,dict_header=None,dict_json=None,params=None,cookies=None,file=None,code=None,res_text=None,res_header=None):


        logger.info("请求方式====>{}".format(method))
        logger.info("请求地址====>{}".format(url))
        logger.info("请求头====>{}".format(json.dumps(dict_header)))
        logger.info("请求参数====>{}".format(json.dumps(params)))
        logger.info("请求体====>{}".format(json.dumps(dict_json)))
        logger.info("上传附件为======>{}".format(file))
        logger.info("Cookies====>{}".format(json.dumps(cookies)))
        logger.info("接口响应状态码====>{}".format(code))
        logger.info("接口响应头为====>{}".format(res_header))
        logger.info("接口响应体为====>{}".format(res_text))




if __name__ == '__main__':
    host = 'https://km.udesk.cn/api'

    op = readexcel('data/testcase.xlsx', 0)

    list = op.Read()

    send=SendRquest()

    for l in list:
        a=send.send_request(host,method=l['method'],url=l['url'],dict_header=l['headers'],dict_json=l['json'],saves=l['saves'],code=l['code'],expect=l['expect'],file=l['file'])
        print(a.json())




