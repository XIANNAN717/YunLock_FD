from selenium.webdriver.common.by import By
from public.po.base_view import BaseView
import logging
from log.log import logger
from public.common.desired_caps import desired
from public.common.do_excel import ReadExcel
from public.po.login_page import OpenWinxin
from public.common.adb_shell import AdbShell
from public.po.new_order_page import NewOderPage
from time import sleep


class TemporaryAuthorization(BaseView):
    # 选择门店按钮
    # shop_xpath = "//*[contains(text(),'测试门店001')]" # no
    # shop_xpath = "//Android.widget.TextView[contains(@text,'测试门店001')]"
    # shop_xpath = "//android.widget.TextView[@text='测试门店001']"
    # shop_xpath = "//*[@class='android.webkit.WebView']/android.widget.View/android.widget.View"
    # shop_xpath = "//*[@class='android.webkit.WebView']/View/View"
    # shop_xpath = "//*[@resource-id='com.tencent.mm:id/kw']/../following-sibling::*[1]//android.widget.View/android.widget.View"
    # shop_xpath = "//*[@resource-id='com.tencent.mm:id/kw']/../following-sibling::*[1]//View/View"
    shop_xpath = "//*[@text='订单管理']" # Y


    shop_btn_element = (By.XPATH , shop_xpath)  # 临时授权按钮元素


    # “选择门店”按钮
    def shop_btn(self):
        shop_btn = self.wait_find_element(*self.shop_btn_element)
        shop_btn.click()


if __name__ == '__main__':
    driver = desired()
    App = OpenWinxin(driver)
    App.click_FD()
    T = TemporaryAuthorization(driver)
    T.shop_btn()

