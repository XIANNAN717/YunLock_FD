import configparser
import os


class ReadConfigIni():
    """
    读取ini文件
    """

    def __init__(self,filename):
        """
        :param filename: ini 文件名
        """
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    def getConfigValue(self,config,name):
        value = self.cf.get(config,name)
        return value


# 调试
if __name__ == '__main__':
    file_path = os.path.split(os.path.realpath(__file__))[0]
    print(file_path)

    read_config = ReadConfigIni(os.path.join(file_path,"config.ini"))
    print(read_config)

    value = read_config.getConfigValue("project","project_path")
    print(value)

