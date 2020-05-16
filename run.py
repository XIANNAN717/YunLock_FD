import pytest
import time
from config import global_config
from public.common import send_mail
import os



if __name__ == '__main__':
    pytest.main(['-sq', '--alluredir', './temp'])
    # 把json文件生成测试报告
    os.system('allure generate ../report/temp -o ../report/test_report  --clean')
    """
    -s 让print的信息可以打印在控制台
    -q 少打印一些版本垃圾信息等不太关注的信息  可以联合一起写 -sq
    --alluredir 生成allure文件地址（这个是json文件，html文件生成需要用这个json文件的参数）
    ./temp  生成json文件位置。
    
    命令（allure generate ./temp -o ./report  --clean）  用allure把上面temp里面的json文件转换成html报告
    转换的路径是 ./report  
    --clean ： 清除其他不必要的文件
    """

