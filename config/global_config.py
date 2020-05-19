import os
from public.common.read_configIni import ReadConfigIni


"""
读取config目录下的ini配置文件，用于获得工程路径
"""

# 获取config.ini所在的路径
file_path = os.path.split(os.path.realpath(__file__))[0]

# 获得cocfig.ini的对象
read_config = ReadConfigIni(os.path.join(file_path, "config.ini"))

# 获得config.ini中的工程路径
project_path = read_config.getConfigValue("project", "project_path")

# 日志路径
log_path = os.path.join(project_path,"report","log")

# 错误截图路径
Images_path = os.path.join(project_path,"report","images")

# 测试用例路径
TestCase_path = os.path.join(project_path,"test_case")

# 测试报告路径
report_path = os.path.join(project_path,"report","test_report")

# 测试数据路径
data_path = os.path.join(project_path,"data")


if __name__ == '__main__':
    print(file_path)
    print(read_config)
    print(project_path)
    print(log_path)
    print(Images_path)
    print(TestCase_path)
    print(Images_path)
    print(data_path)