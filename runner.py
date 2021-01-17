#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tao
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tao
import sys

import pytest
from common import configUtil
from common import shell

if __name__ == '__main__':

    conf = configUtil.Config()
    shell = shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path
    test_case_path   = conf.test_case_path
    args = ['-s', '-q',test_case_path,'--alluredir', "report/xml",'--clean-alluredir']

    pytest.main(args)
    cmd = 'allure generate %s -o %s --clean' % ("report/xml", "report/html")

    # try:
    #     shell.invoke(cmd)
    # except Exception:
    #     raise