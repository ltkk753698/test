#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tao
import jsonpath
from common.Readexcel import readexcel
from common.Sendrequest import SendRquest
import pytest
from common.configUtil import Config
import allure

from common.logger import LoggerHandler

conf=Config()
env=conf.get_value("run.conf", "exec", "env")
data=conf.get_value("run.conf", "exec", "data")
num=conf.get_value("run.conf", "exec", "num")
log_dir = conf.get_value("log.conf", "basiclog", "log_dir")
format = conf.get_value("log.conf", "basiclog", "format")
host = conf.get_value("host.conf", env, "host")
op = readexcel(data,int(num))

list = op.Read()

logger=LoggerHandler(file=log_dir,format=format)

data=[]
for l in list:
    data.append(pytest.param(host, l["url"], l["method"],l["json"],l["headers"],l["saves"],l["code"],l["expect"],l['file'],id=l["id"]))

send=SendRquest()

@allure.story()
@pytest.mark.parametrize("host, method, url, dict_json, dict_header, saves,code,expect,file",data)
def test_api(host, method, url, dict_json, dict_header,saves, code,expect,file):

    res =send.send_request(host,method,url,dict_json=dict_json,dict_header=dict_header,saves=saves)

    assert res.status_code == code
    logger.info("断言成功,实际code值：{} = 预期code值：{}".format(res.status_code, code))

    if "$" in expect:
        expect =expect.split(';')
        for exp in expect:
            #提取jsonpath
            jsp=exp.split('=')[0]
            actual=jsonpath.jsonpath(res.json(),jsp)[0]

            expc=eval(exp.split('=')[1])
            assert actual == expc

            logger.info("断言成功,实际值：{} = 预期值：{}".format(actual, expc))

    else:
            assert expect in res.text
            logger.info("断言成功,预期值：{} 包含于实际值：{}".format(expect, res.text))






