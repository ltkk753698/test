#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tao

import logging
import time

import os


class LoggerHandler(logging.Logger):

    def __init__(self,
                 name='python',
                 level='INFO',
                 file=None,
                 format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'):

        super().__init__(name)

        #设置级别
        self.setLevel(level)

        fmt=logging.Formatter(format)

        #初始化处理器
        if file:
            cur_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            #package_path = os.path.abspath("..")
            package_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(package_path, file)
            file_name = cur_date + ".txt"
            log_file = os.path.join(file_path, file_name)
            file_handler=logging.FileHandler(log_file)
            file_handler.setLevel(level)

            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        steam_handler=logging.StreamHandler()
        # 设置handler级别
        steam_handler.setLevel(level)

        steam_handler.setFormatter(fmt)
        self.addHandler(steam_handler)



if __name__ == '__main__':
    logger=LoggerHandler()
    logger.info('hello')




