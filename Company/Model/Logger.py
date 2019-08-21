# -*- coding: utf-8 -*-
import logging
import os.path
import platform
import time
from Model.FileUtils import FileUtils


class Logger(object):

    def __init__(self, logger1):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger1:
        """
        # 创建日志名称。
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))
        log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/Log/log/'
        # print(log_path)
        # print(platform.system())
        if 'Windows' in platform.system():
            # windows os
            log_path = log_path.replace('/', '\\')
        FileUtils().mkdir(log_path)

        # 创建一个logger
        self.logger = logging.getLogger(logger1)
        self.logger.setLevel(logging.DEBUG)
        log_name = log_path + logger1 + '.log'
        # 创建一个handler，用于写入日志文件
        self.fh = logging.FileHandler(filename=log_name, mode='a', encoding='utf-8')
        self.fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
        formatter = logging.Formatter('%(asctime)s %(filename)s %(name)s [line:%(lineno)d] %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')
        self.fh.setFormatter(formatter)
        # ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(self.fh)
        # self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

if __name__ == "__main__":
    pass
