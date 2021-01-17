#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tao
import sys

import pytest
from common.configUtil import Config
from common.shell import Shell

if __name__ == '__main__':
    conf = Config()
    shell = Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path
    test_case_path   = conf.test_case_path
    args = ['-s', '-q',test_case_path, '--alluredir', xml_report_path,'--clean-alluredir']
    self_args = sys.argv[1:]
    pytest.main(args)
    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)

    try:
        shell.invoke(cmd)
    except Exception:
        raise