from public.po.base_view import BaseView
import logging
from log.log import logger
from public.common.desired_caps import desired
from time import sleep

# 日志类的实例化
logger = logger(__name__, Cmdlevel=logging.INFO, Filelevel=logging.INFO)


class OpenWinxin(BaseView):

    def __init__(self, driver):
        super().__init__(driver)

    # 打开微信
    def open_weixin(self):
        try:
            sleep(5)
            # 下滑，进入微信小程序页面
            self.swipe_down()
            logger.info("打开微信，进入小程序页面成功")
        except:
            logger.info("打开微信失败")



    # 点击最近使用里的房东小程序
    def click_FD(self):
        self.open_weixin()
        sleep(3)
        self.click_img(r'entrance\FD.png')
        logger.info("FDBtn is click")



# 调试
if __name__ == '__main__':
    driver = desired()
    weixin = OpenWinxin(driver)
    weixin.click_FD()
