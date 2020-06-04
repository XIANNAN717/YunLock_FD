# -*- coding: gb18030 -*-
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from public.po.base_view import BaseView
import logging
from log.log import logger
from public.common.desired_caps import desired
from public.common.do_excel import ReadExcel
from public.po.login_page import OpenWinxin
from public.common.adb_shell import AdbShell
from time import sleep

# 日志类的实例化
logger = logger(__name__, Cmdlevel=logging.INFO, Filelevel=logging.INFO)


class NewOderPage(BaseView):
    """
    新建订单页面的所有的xpth、元素
    """
    # 订单管理
    oder_management_xpath = "//*[@text='订单管理']"
    # 选择房间
    choose_room_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.widget.Image"
    # 选择房间确定按钮
    room_confirm_xpath = "//*[@text='确定']"
    # 入住时间
    checkin_time_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View[1]"
    # 选择时间确认按钮
    time_confirm = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[14]"
    # 退房时间
    checkout_time_xpath = "//*[@text='请选择离店时间']"
    # 入住人姓名
    tenant_name_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View[5]/android.view.View/android.view.View"
    # 入住人手机号
    tenant_mobile_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View[7]/android.view.View/android.view.View"
    # 订单来源
    order_source_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View[9]/android.view.View[2]"
    # 房费总计
    room_rate_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View[11]/android.view.View/android.view.View"
    # 备注信息
    remark_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View[13]/android.view.View/android.view.View"
    # 确定按钮
    confirm_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View[14]"

    # 元素定位
    oder_management_btn_element = (By.XPATH, oder_management_xpath)  # 订单管理
    choose_room_element = (By.XPATH, choose_room_xpath)  # 选择房间
    room_confirm_element = (By.XPATH, room_confirm_xpath)  # 第一个房间
    checkin_time_element = (By.XPATH, checkin_time_xpath)  # 入住时间
    time_confirm_element = (By.XPATH, time_confirm)  # 选择时间的确认按钮
    checkout_time_element = (By.XPATH, checkout_time_xpath)  # 退房时间
    tenant_name_element = (By.XPATH, tenant_name_xpath)  # 入住人姓名
    tenant_mobile_element = (By.XPATH, tenant_mobile_xpath)  # 入住人手机号
    order_source_element = (By.XPATH, order_source_xpath)  # 订单来源
    room_rate_element = (By.XPATH, room_rate_xpath)  # 房屋价格
    remark_element = (By.XPATH, remark_xpath)  # 备注信息
    confirm_element = (By.XPATH, confirm_btn_xpath)  # 确定按钮

    def __init__(self, driver):
        super().__init__(driver)

    # “订单管理”按钮
    def oder_management(self):
        oder_management_btn = self.wait_find_element(*self.oder_management_btn_element)
        oder_management_btn.click()
        logger.info("OderManagementBtn is click")

    # 新建订单按钮
    def click_new_order(self):
        sleep(3)
        self.click_img(r'entrance\NO.png')
        logger.info("new_order_Btn is click")

    # 选择房间
    def choose_room(self):
        choose_room = self.wait_find_element(*self.choose_room_element)
        choose_room.click()
        self.wait_find_element(*self.room_confirm_element).click()
        logger.info("ChooseRoom is click")

    # 入住开始时间
    def checkin_time(self):
        checkin_time = self.wait_find_element(*self.checkin_time_element)
        checkin_time.click()
        self.wait_find_element(*self.time_confirm_element).click()
        logger.info("checkin_time is click")

    # 入住结束时间
    def checkout_time(self):
        checkout_time = self.wait_find_element(*self.checkout_time_element)
        # checkout_time.click()
        self.unlock_swipe_up()
        self.wait_find_element(*self.time_confirm_element).click()
        logger.info("checkin_time is click")

    # “入住人姓名”文本区域
    def tenant_name(self, tenant_name_value):
        tenant_name_text = self.wait_find_element(*self.tenant_name_element)  # 户型描述输入
        tenant_name_text.click()
        AdbShell.input_text(tenant_name_value)
        # print("入住人姓名：",tenant_name_value)
        # tenant_name_text.send_keys(tenant_name_value)
        logger.info("TenantNameText is setValues!")


    # “入住人手机号”文本区域
    def tenant_mobile(self, tenant_mobile_value):
        tenant_mobile_text = self.wait_find_element(*self.tenant_mobile_element)  # 户型描述输入
        tenant_mobile_text.click()
        AdbShell.input_text(tenant_mobile_value)
        logger.info("TenantMobileText is setValues!")


    # 提交订单时的“确定”按钮
    def confirm_button(self):
        ConfirmBtn = self.wait_find_element(*self.confirm_element)
        ConfirmBtn.click()
        logger.info("ConfirmBtn is click")

    # 新建订单流程
    def new_order(self):
        try:
            tenant_name_value = ReadExcel("new_order.xlsx", "Sheet1").read_excel(1, 0)
            tenant_mobile_value = ReadExcel("new_order.xlsx", "Sheet1").read_excel(1, 1)
            self.oder_management()
            self.click_new_order()
            # self.choose_room()
            # self.checkin_time()
            # self.checkout_time()
            self.tenant_name(tenant_name_value)
            self.tenant_mobile(tenant_mobile_value)
            self.confirm_button()
            return "新建订单成功"
        except:
            print("新建订单失败")
            self.get_screeShot()



if __name__ == '__main__':
    driver = desired()
    App = OpenWinxin(driver)
    App.open_weixin()
    App.click_FD()
    FD_new_order = NewOderPage(driver)
    # FD_new_order.oder_management()
    # FD_new_order.click_new_order()
    FD_new_order.new_order()