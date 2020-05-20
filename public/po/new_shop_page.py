# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from public.po.base_view import BaseView
import logging
from log.log import logger
from public.common.desired_caps import desired
from public.common.do_excel import ReadExcel
from public.po.login_page import LoginPage
from public.common.adb_shell import AdbShell
from time import sleep


# 日志类的实例化
logger = logger(__name__, Cmdlevel=logging.INFO, Filelevel=logging.INFO)

class NewShopPage(BaseView):
    mine_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View"
    shop_management_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]"
    shop_name_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText"
    confirm_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.Button"

    mine_element = (By.XPATH, mine_xpath)
    shop_management_element = (By.XPATH, shop_management_xpath)
    new_shop_btn_element = (By.XPATH, "//*[@text='新建门店']")
    shop_name_element = (By.XPATH, shop_name_xpath)
    confirm_element = (By.XPATH, confirm_btn_xpath)


    def __init__(self,driver):
        super().__init__(driver)

    # “我的”按钮
    def mine(self):
        mine_element_btn = self.wait_find_element(*self.mine_element)
        mine_element_btn.click()
        logger.info("MineElementBtn is click!")


    # “门店管理”按钮
    def shop_management(self):
        shop_management_btn = self.wait_find_element(*self.shop_management_element)  # 户型描述输入
        shop_management_btn.click()
        logger.info("ShopManagementValue is click!")


    # “新建门店”按钮
    def new_shop_btn(self):
        new_shop_btn = self.wait_find_element(*self.new_shop_btn_element)
        sleep(1)
        new_shop_btn.click()
        logger.info("NewShopBtn is click!")


    # “新建门店名称”文本输入框
    def shop_name(self, shop_name_Value):
        shop_name_text = self.wait_find_element(*self.shop_name_element)
        shop_name_text.click()
        AdbShell.input_text(shop_name_Value)
        logger.info("RoomDescriptionText is setValues!")
        self.get_screeShot()


   # 确定按钮
    def confirm_button(self):
        ConfirmBtn = self.wait_find_element(*self.confirm_element)
        ConfirmBtn.click()
        logger.info("ConfirmBtn is click")

    # 新建门店流程
    def new_shop(self):
        try:
            self.wait_activity(".MainActivity", 30)
            self.mine()
            self.shop_management()
            self.new_shop_btn()
            read_excel = ReadExcel("new_shop.xlsx", "Sheet1")
            shop_name_Value = read_excel.read_excel(1, 0)
            self.shop_name(shop_name_Value)
            self.confirm_button()
            return "新建门店成功"
        except:
            print("新建门店失败")



if __name__ == '__main__':
    driver = desired()
    App = LoginPage(driver)
    App.login()
    YunLock_new_shop = NewShopPage(driver)
    YunLock_new_shop.new_shop()


