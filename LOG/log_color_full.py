import logging
from logging import handlers
from colorama import Fore, Style
import os
import sys

# 获取对象
def get_logger():
    logger = logging.getLogger("all1.log")
    logger.setLevel(logging.DEBUG)
 

    if not logger.handlers:
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = ColoredFormatter(
            '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        )

       
  
        ch.setFormatter(formatter)
        fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        format_str_inlog = logging.Formatter(fmt)#设置日志格式

        when='D'
        backCount=3

        th = handlers.TimedRotatingFileHandler(filename="all1.log",when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str_inlog)#设置文件里写入的格式

        logger.addHandler(ch)
        logger.addHandler(th)
    
    return logger

# 自定义 Formatter
class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': Fore.WHITE,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Style.BRIGHT
    }

    def format(self, record):
        log_message = super(ColoredFormatter, self).format(record)
        log_level_color = self.COLORS.get(record.levelname, Fore.RESET)
        return f'{log_level_color}{log_message}{Style.RESET_ALL}'

#通过静态成员方法来调用
class Log:

    logger = get_logger()

    @staticmethod
    def debug(msg):
        Log.logger.debug("[DEBUG]: " + str(msg))

    @staticmethod
    def info(msg):
        Log.logger.info("[INFO]: " + str(msg))

    @staticmethod
    def warning(msg):
        Log.logger.warning("[WARNING]: " + str(msg))

    @staticmethod
    def error(msg):
        Log.logger.error("[ERROR]: " + str(msg))

    @staticmethod
    def critical(msg):
        Log.logger.critical("[CRITICAL]: " + str(msg))

Log.debug("hello")
Log.info("hello")
Log.warning("hello")
Log.critical("hello")
