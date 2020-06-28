import os

import requests

from code.func import get_data_path


class DanmukuHistory(object):
    def __init__(self, **args):
        # 初始化
        code_name = os.path.realpath(__file__)
        self.data_name = get_data_path(code_name)
        # 参数获取
        self.av = args.get("av")
        self.start_day = args.get("start_day")
        self.end_day = args.get("end_day")
        # 获取所有
        self.get_all()
        
    def get_oid(self):
        """根据提供的av号获取对应的oid"""
        pass
    
    def get_driver(self):
        pass
        
    def get_per_day(self):
        pass
        
    def get_all_day(self):
        pass

    
    def get_all(self):
        """运行所有"""
        self.get_oid()
        
def run(**args):
    DanmukuHistory(**args)
