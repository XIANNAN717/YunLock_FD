"""
一、人工认证入口
    1 进入订单管理、全部订单界面
    2 获取全部订单列表中的所有订单的状态
    3 如果订单状态为“入住中”且“待认证”
    4 点击进入该订单详情界面
    5 点击“人工认证”，进入人工认证界面
二、人工认证参数
    1 选择名族
    2 输入证件号
    3 输入住址
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

class ArtificialAuthenticationPage(BaseView):
    # “全部订单”按钮xpath
    all_order_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[6]"
    # 订单列表第一个
    order_list_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View"
    # 人工认证按钮
    artificial_authentication_btn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.view.View/android.view.View[3]/android.widget.Button"
    # "选择名族"按钮xpath
    choose_ethnic_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]"
    # 名族名称（第一个）xpath
    ethnic_name_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]"
    # 证件号xpath
    id_number_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[3]"
    # 住址xpath
    address_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[4]"
    # 确定按钮
    confirm_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]/android.widget.Button"

    all_order_btn_element = (By.XPATH , all_order_btn_xpath) # 全部订单按钮元素
    order_list_element = (By.XPATH , order_list_xpath)  # 订单列表中的第一个订单
    artificial_authentication_btn_element = (By.XPATH , artificial_authentication_btn)  # 人工认证按钮元素
    choose_ethnic_element = (By.XPATH ,choose_ethnic_xpath)  # 选择名族的元素
    ethnic_name_element = (By.XPATH , ethnic_name_xpath)  # 名族名称元素
    id_number_element = (By.XPATH ,id_number_xpath)  # 证件号元素
    address_element = (By.XPATH , address_xpath)  # 地址元素
    confirm_btn_element = (By.XPATH , confirm_btn_xpath)  # 确定按钮元素

    # “全部订单”按钮
    def all_order_btn(self):
        all_order_btn = self.wait_find_element(*self.all_order_btn_element)
        all_order_btn.click()
        logger.info("AllOrderBtn is click")

    #  订单列表
    def order_list(self):
        order_list = self.wait_find_element(*self.order_list_element)
        order_list.click()
        logger.info("OrderList is click")

    # 人工认证按钮
    def artificial_authentication_btn(self):
        artificial_authentication_btn = self.wait_find_element(*self.artificial_authentication_btn_element)
        artificial_authentication_btn.click()
        logger.info("artificial_authentication_btn is click")

    # 选择名族
    def choose_ethnic_btn(self):
        choose_ethnic = self.wait_find_element(*self.choose_ethnic_element)
        choose_ethnic.click()
        ethnic_name = self.wait_find_element(*self.ethnic_name_element)
        ethnic_name.click()
        logger.info("Ethnic is click")

    # 证件号输入框
    def id_number_input_box(self,id_number_value):
        id_number = self.wait_find_element(*self.id_number_element)
        id_number.click()
        AdbShell.input_text(id_number_value)
        logger.info("IdNumber is SetValue")

    # 住址输入框
    def address_input_box(self,address_value):
        address = self.wait_find_element(*self.address_element)
        address.click()
        AdbShell.input_text(address_value)
        logger.info("Address is SetValue")

    # 提交人工认证“确定”按钮
    def confirm_btn(self):
        confirm_btn = self.wait_find_element(*self.confirm_btn_element)
        confirm_btn.click()
        logger.info("Confirm is click")

    # 人工认证流程
    def artificial_authentication_Process(self):
        try:
            NewOder = NewOderPage(self.driver)
            NewOder.oder_management()
            NewOder.choose_shop()
            self.all_order_btn()
            self.order_list()
            self.artificial_authentication_btn()
            self.choose_ethnic_btn()
            id_number_value = ReadExcel("artificial_authentication.xlsx", "Sheet1").read_excel(1, 0)
            self.id_number_input_box(id_number_value)
            address_value = ReadExcel("artificial_authentication.xlsx", "Sheet1").read_excel(1, 1)
            print(address_value)
            self.address_input_box(address_value)
            self.confirm_btn()
            return "人工认证成功"
        except:
            print("人工认证失败")



if __name__ == '__main__':
    driver = desired()
    App = LoginPage(driver)
    App.login()
    # NewOder = NewOderPage(driver)
    # NewOder.oder_management()
    # NewOder.choose_shop()
    AA = ArtificialAuthentication(driver)
    AA.artificial_authentication_Process()

