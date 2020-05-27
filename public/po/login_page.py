from selenium.webdriver.common.by import By
from public.common.desired_caps import desired
from public.po.base_view import BaseView
from log.log import logger
import logging
from time import sleep


# 日志类的实例化
logger = logger(__name__, Cmdlevel=logging.INFO, Filelevel=logging.INFO)


class LoginPage(BaseView):
    YunLock_xpath = "//android.widget.FrameLayout[@content-desc='当前所在页面,与的聊天']/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.ImageView[2]"

    YunLock_text_element = (By.XPATH, YunLock_xpath)

    def __init__(self, driver):
        super().__init__(driver)

    def YunLock_click(self):
        YunLock_text = self.wait_find_element(*self.YunLock_text_element)
        YunLock_text.click()




# 调试
if __name__ == '__main__':
    des = desired()
    b = BaseView(des)
    sleep(5)
    b.swipe_down()
    open_YunLock = LoginPage(des)
    open_YunLock.YunLock_click()
