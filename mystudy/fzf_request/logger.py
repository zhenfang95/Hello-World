#coding:utf-8
import logging
class Loger():
    def __init__(self):
        self.logger = logging.getLogger()
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = "test.log"
        #日志输出级别
        self.console_output_level = "INFO"
        self.file_output_level = "DEBUG"
        #日志输出格式
        self.formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s - %(message)s")
    def get_logger(self):
        '''封装logger'''
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            file_handler = logging.FileHandler(self.log_file_name)
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.console_output_level)
            self.logger.addHandler(file_handler)
            return self.logger
logger = Loger().get_logger()
