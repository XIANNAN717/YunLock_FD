# -*- coding: gb18030 -*-
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


class NewOderPage(BaseView):
    """
    新建订单页面的所有的xpth、元素
    """
    # 订单管理
    oder_management_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View"
    # 选择门店
    choose_shop_xapth = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]"
    # 测试门店第二个门店
    test_shop_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]"
    # 新建订单按钮
    new_oder_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button"
    # 选择房间
    choose_room_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[1]/android.view.View[1]"
    # 测试房源第一个
    test_room_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]"
    # 入住时间
    checkin_time_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[1]/android.view.View[2]/android.widget.Button[1]"
    # 选择时间确认按钮
    time_confirm = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button[2]"
    # 退房时间
    checkout_time_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[1]/android.view.View[2]/android.widget.Button[2]"
    # 入住人姓名
    tenant_name_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText[1]"
    # 入住人手机号
    tenant_mobile_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText[2]"
    # 订单来源
    order_source_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[5]"
    # 房费总计
    room_rate_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText[3]"
    # 备注信息
    remark_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText[4]"
    # 确定按钮
    confirm_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button"

    # 元素定位
    oder_management_btn_element = (By.XPATH, oder_management_xpath)  # 订单管理
    shop_btn_element = (By.XPATH, choose_shop_xapth)  # 选择门店
    test_shop_element = (By.XPATH, test_shop_xpath)  # 第二个门店
    new_oder_btn_element = (By.XPATH, new_oder_btn_xpath)  # 新建订单按钮
    choose_room_element = (By.XPATH, choose_room_xpath)  # 选择房间
    test_room_element = (By.XPATH, test_room_xpath)  # 第一个房间
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

    # “选择门店”按钮
    def choose_shop(self):
        shop_btn = self.wait_find_element(*self.shop_btn_element)
        shop_btn.click()
        # print('开始滑动')
        # sleep(5)
        # self.swipe_up(450, 1500, 450, 1200)
        shop_name = self.wait_find_element(*self.test_shop_element)
        shop_name.click()
        logger.info("ChooseShopBtn is click")

    # “新建订单”按钮
    def new_oder_btn(self):
        new_oder_btn = self.wait_find_element(*self.new_oder_btn_element)
        new_oder_btn.click()
        logger.info("NewOderBtn is click")

    # 选择房间
    def choose_room(self):
        choose_room = self.wait_find_element(*self.choose_room_element)
        # print(choose_room)
        choose_room.click()
        room_name = self.wait_find_element(*self.test_room_element)
        # print(room_name)
        room_name.click()
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
        checkout_time.click()
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
            # self.choose_shop()
            self.new_oder_btn()
            self.choose_room()
            self.checkin_time()
            self.checkout_time()
            self.tenant_name(tenant_name_value)
            self.tenant_mobile(tenant_mobile_value)
            self.confirm_button()
            return "新建订单成功"
        except:
            print("新建订单失败")
            self.get_screeShot()



if __name__ == '__main__':
    driver = desired()
    App = LoginPage(driver)
    App.login()
    YunLock_new_order = NewOderPage(driver)
    YunLock_new_order.new_order()