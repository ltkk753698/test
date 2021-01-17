#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Chris
import configparser
import os

# path
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
print(path_dir)

class Config:
    def __init__(self):
        self.config_folder = "Config"
        self.xml_report_path = path_dir + r'\report\xml'
        self.html_report_path = path_dir + r'\report\html'
        self.test_case_path   = path_dir + r'\testcase\test_case.py'
    '''
        读取配置文件
        :param file_name:配置文件名称
        :param section:配置文件中的section
        :param key:配置文件中的key
    '''
    def get_value(self, file_name, section, key):
        try:
            config = self.get_config_file(file_name)
            value = config.get(section, key)
            return value
        except Exception as e:
            print("get value failed:" + str(e))

    '''
        写入配置文件
        :param file_name:配置文件名称
        :param section:配置文件中的section
        :param key:配置文件中的key
        :param value:配置文件中的key对应的value
    '''
    def set_value(self, file_name, section, key, value):
        try:
            config = self.get_config_file(file_name)
            config.add_section(section)
            config.set(section, key, value)
            config.write(open(self.get_file_path(self.config_folder, file_name), "w+"))
        except Exception as e:
            print("set value failed:" + str(e))

    '''
        修改配置文件
        :param file_name:配置文件名称
        :param section:配置文件中的section
        :param key:配置文件中的key
        :param value:配置文件中的key对应的value
    '''
    def update_value(self, file_name, section, key, value):
        try:
            config = self.get_config_file(file_name)
            config.set(section, key, value)
            config.write(open(self.get_file_path(self.config_folder, file_name), "r+"))
        except Exception as e:
            print("update value failed:" + str(e))

    '''
        移除配置文件中某个key
        :param file_name:配置文件名称
        :param section:配置文件中的section
        :param key:配置文件中的key
    '''
    def remove_option(self, file_name, section, key):
        try:
            config = self.get_config_file(file_name)
            config.remove_option(section, key)
            config.write(open(self.get_file_path(self.config_folder, file_name), "r+"))
        except Exception as e:
            print("remove key failed:" + str(e))

    '''
        移除配置文件中某个section
        :param file_name:配置文件名称
        :param section:配置文件中的section
    '''
    def remove_section(self, file_name, section):
        try:
            config = self.get_config_file(file_name)
            config.remove_section(section)
            config.write(open(self.get_file_path(self.config_folder, file_name), "r+"))
        except Exception as e:
            print("remove section failed:" + str(e))

    '''
        读取配置文件
        :param file_name:配置文件名称
    '''
    def get_config_file(self, file_name):
        try:
            config = configparser.ConfigParser()
            file_path = self.get_file_path(self.config_folder, file_name)
            config.read(file_path)
            return config
        except Exception as e:
            print("read config file error:" + str(e))

    '''
        读取文件所在路径，默认读取Config文件夹的文件，如需修改，实例化类时，传文件夹名称
        注意：只能读取com.note包及子包下的文件
        :param file_name:文件名称
    '''
    @staticmethod
    def get_file_path(folder_name, file_name):
        config_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(config_path, folder_name,file_name)

        return file_path


if __name__ == '__main__':
    conf = Config()
    # print(sys.argv[0])
    # print(conf.get_value("sign.conf", "product", "api_token"))
    # print(conf.get_value("sign.conf", "test", "api_token"))
    print(conf.test_case_path)
