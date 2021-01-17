#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tao


import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("gb2312")
        return o