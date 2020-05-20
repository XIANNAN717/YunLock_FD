"""
一、临时授权入口
    1、临时授权按钮
    2、添加授权按钮
二、临时授权参数
    1、选择时间
    2、被授权人姓名
    3、被授权人手机号
    4、被授权人身份
"""

from selenium.webdriver.common.by import By
from public.po.base_view import BaseView
import logging
from log.log import logger
from public.common.desired_caps import desired
from public.common.do_excel import ReadExcel
from public.po.login_page import LoginPage
from public.common.adb_shell import AdbShell
from public.po.new_order_page import NewOderPage

# 日志类的实例化
logger = logger(__name__, Cmdlevel=logging.INFO, Filelevel=logging.INFO)

class TemporaryAuthorization(BaseView):
    # 临时授权按钮xpath
    temporary_authorization_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button[1]"
    # 添加授权按钮xpath
    add_authorization_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]"
    # 入住时间xpath
    checkin_time_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.Button[1]"
    # 选择时间“确定”按钮
    time_confirm = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button[2]"
    # 退房时间
    checkout_time_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.Button[2]"
    # 被授权人姓名
    authorized_name_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]"
    # 被授权人手机号
    authorized_mobile_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]"
    # 被授权人身份按钮
    authorized_identity_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]"
    # 被授权人身份（列表第二个元素，保洁）
    authorized_identity_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]"
    # 提交授权确定按钮
    confirm_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button"

    temporary_authorization_btn_element = (By.XPATH , temporary_authorization_btn_xpath)  # 临时授权按钮元素
    add_authorization_btn_element = (By.XPATH , add_authorization_btn_xpath)  # 添加临时授权按钮元素
    checkin_time_element = (By.XPATH, checkin_time_xpath)  # 入住时间
    time_confirm_element = (By.XPATH, time_confirm)  # 选择时间的确认按钮
    checkout_time_element = (By.XPATH, checkout_time_xpath)  # 退房时间
    authorized_name_element = (By.XPATH , authorized_name_xpath)  # 被授权人姓名元素
    authorized_mobile_element = (By.XPATH , authorized_mobile_xpath)  # 被授权人手机号元素
    authorized_identity_btn_element = (By.XPATH , authorized_identity_btn_xpath)  # 被授权人身份元素
    authorized_identity_element = (By.XPATH , authorized_identity_xpath)  # 被授权人身份（列表第二个元素，保洁）
    confirm_btn_element = (By.XPATH , confirm_btn_xpath)   # 提交临时授权“确定”按钮


    # “临时授权”按钮
    def temporary_authorization_btn(self):
        temporary_authorization_btn = self.wait_find_element(*self.temporary_authorization_btn_element)
        temporary_authorization_btn.click()
        logger.info("temporary_authorization_btn is click")

    # “添加临时授权”按钮
    def add_authorization_btn(self):
        add_authorization_btn = self.wait_find_element(*self.add_authorization_btn_element)
        add_authorization_btn.click()
        logger.info("add_authorization_btn is click")

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

    # 被授权人姓名输入框
    def authorized_name_input_box(self,authorized_name_value):
        authorized_name_text = self.wait_find_element(*self.authorized_name_element)
        authorized_name_text.click()
        AdbShell.input_text(authorized_name_value)
        logger.info("authorized_name_text is SetValue")

    # 被授权人手机号输入框
    def authorized_mobile_input_box(self, authorized_mobile_value):
        authorized_mobile_text = self.wait_find_element(*self.authorized_mobile_element)
        authorized_mobile_text.click()
        AdbShell.input_text(authorized_mobile_value)
        logger.info("authorized_mobile is SetValue")

    # 选择被授权人身份
    def authorized_identity_btn(self):
        # 被授权人身份按钮
        authorized_identity_btn = self.wait_find_element(*self.authorized_identity_btn_element)
        authorized_identity_btn.click()
        # 被授权人身份（列表第二个元素，保洁）
        authorized_identity = self.wait_find_element(*self.authorized_identity_element)
        authorized_identity.click()
        logger.info("authorized_identity is click")

    # 提交临时授权“确定”按钮
    def confirm_btn(self):
        confirm_btn = self.wait_find_element(*self.confirm_btn_element)
        confirm_btn.click()
        logger.info("Confirm is click")

    # 临时授权流程
    def temporary_authorization_process(self):
        try:
            YunLock_new_order = NewOderPage(self.driver)
            YunLock_new_order.choose_shop()
            self.temporary_authorization_btn()
            self.add_authorization_btn()
            self.checkin_time()
            self.confirm_btn()
            self.checkout_time()
            self.confirm_btn()
            authorized_name_value = ReadExcel("temporary_authorization.xlsx", "Sheet1").read_excel(1, 0)
            self.authorized_name_input_box(authorized_name_value)
            authorized_mobile_value = ReadExcel("temporary_authorization.xlsx", "Sheet1").read_excel(1, 1)
            self.authorized_mobile_input_box(authorized_mobile_value)
            self.authorized_identity_btn()
            self.confirm_btn()
            return "临时授权成功"
        except:
            print("临时授权失败")



if __name__ == '__main__':
    driver = desired()
    App = LoginPage(driver)
    App.login()
    TA = TemporaryAuthorization(driver)
    YunLock_new_order = NewOderPage(driver)
    YunLock_new_order.choose_shop()
    TA.temporary_authorization_btn()
    TA.add_authorization_btn()
    TA.checkin_time()
    TA.confirm_btn()
    TA.checkout_time()
    TA.confirm_btn()
    authorized_name_value = ReadExcel("temporary_authorization.xlsx", "Sheet1").read_excel(1, 0)
    TA.authorized_name_input_box(authorized_name_value)
    authorized_mobile_value = ReadExcel("temporary_authorization.xlsx", "Sheet1").read_excel(1, 1)
    TA.authorized_mobile_input_box(authorized_mobile_value)
    TA.authorized_identity_btn()
    TA.confirm_btn()
