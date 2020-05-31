# -*- coding: gb18030 -*-
# -*- coding: utf-8 -*-
from appium import webdriver

ServerUrl = 'http://127.0.0.1:4723/wd/hub'


def desired():
    desired_caps = {
        'noReset': True,  # 驱动APP，不要清除app里的原有的数据
        'fullReset' : False,
        'platformName': 'Android',
        'platformVersion': '5.1',
        # 'unicodeKeyboard': True,  # 使用Unicode输入法
        'resetKeyboard': True,  # 重置输入法到初始状态
       #'deviceName': 'WTKDU16C07002694',
        'deviceName':'127.0.0.1:62001',
        'appPackage': 'com.upqing.sunflower',
        # 'appPackage': 'com.tencent.mm',
        'appActivity': '.MainActivity',
        # 'appActivity': '.ui.LauncherUI'

    }
    driver = webdriver.Remote(ServerUrl, desired_caps)
    return driver


# 调试
if __name__ == '__main__':
    des = desired()
