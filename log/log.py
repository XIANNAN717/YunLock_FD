import logging
import os
import time
from config import global_config


log_path = global_config.log_path
# print(log_path)


class logger():
    def __init__(self,logger,Cmdlevel,Filelevel):
        """
        :param logger:
        :param Cmdlevel:
        :param Filelevel:
        """
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # 设定日志文件的名称
        # 存放在log类所在的当前目录
        # 将日志存放在指定的日志路径下

        self.logFileName = os.path.join(log_path,"{0}.log".format(time.strftime("%Y-%m-%d-%H")))

        # 设置控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(Cmdlevel)

        # 设置文件日志
        fh = logging.FileHandler(self.logFileName)
        fh.setFormatter(fmt)
        fh.setLevel(Filelevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    logger = logger(__name__,Cmdlevel=logging.INFO,Filelevel=logging.ERROR)
    logger.debug("debug message")
    logger.info("info message")
    logger.war("warning message")
    logger.error("error message")
    logger.cri("critical message")

