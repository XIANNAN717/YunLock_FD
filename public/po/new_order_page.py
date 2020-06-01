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

# ��־���ʵ����
logger = logger(__name__, Cmdlevel=logging.INFO, Filelevel=logging.INFO)


class NewOderPage(BaseView):
    """
    �½�����ҳ������е�xpth��Ԫ��
    """
    # ��������
    oder_management_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View"
    # ѡ���ŵ�
    choose_shop_xapth = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]"
    # �����ŵ�ڶ����ŵ�
    test_shop_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]"
    # �½�������ť
    new_oder_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button"
    # ѡ�񷿼�
    choose_room_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[1]/android.view.View[1]"
    # ���Է�Դ��һ��
    test_room_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]"
    # ��סʱ��
    checkin_time_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[1]/android.view.View[2]/android.widget.Button[1]"
    # ѡ��ʱ��ȷ�ϰ�ť
    time_confirm = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button[2]"
    # �˷�ʱ��
    checkout_time_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[1]/android.view.View[2]/android.widget.Button[2]"
    # ��ס������
    tenant_name_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText[1]"
    # ��ס���ֻ���
    tenant_mobile_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText[2]"
    # ������Դ
    order_source_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View[5]"
    # �����ܼ�
    room_rate_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText[3]"
    # ��ע��Ϣ
    remark_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText[4]"
    # ȷ����ť
    confirm_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button"

    # Ԫ�ض�λ
    oder_management_btn_element = (By.XPATH, oder_management_xpath)  # ��������
    shop_btn_element = (By.XPATH, choose_shop_xapth)  # ѡ���ŵ�
    test_shop_element = (By.XPATH, test_shop_xpath)  # �ڶ����ŵ�
    new_oder_btn_element = (By.XPATH, new_oder_btn_xpath)  # �½�������ť
    choose_room_element = (By.XPATH, choose_room_xpath)  # ѡ�񷿼�
    test_room_element = (By.XPATH, test_room_xpath)  # ��һ������
    checkin_time_element = (By.XPATH, checkin_time_xpath)  # ��סʱ��
    time_confirm_element = (By.XPATH, time_confirm)  # ѡ��ʱ���ȷ�ϰ�ť
    checkout_time_element = (By.XPATH, checkout_time_xpath)  # �˷�ʱ��
    tenant_name_element = (By.XPATH, tenant_name_xpath)  # ��ס������
    tenant_mobile_element = (By.XPATH, tenant_mobile_xpath)  # ��ס���ֻ���
    order_source_element = (By.XPATH, order_source_xpath)  # ������Դ
    room_rate_element = (By.XPATH, room_rate_xpath)  # ���ݼ۸�
    remark_element = (By.XPATH, remark_xpath)  # ��ע��Ϣ
    confirm_element = (By.XPATH, confirm_btn_xpath)  # ȷ����ť

    def __init__(self, driver):
        super().__init__(driver)

    # ������������ť
    def oder_management(self):
        oder_management_btn = self.wait_find_element(*self.oder_management_btn_element)
        oder_management_btn.click()
        logger.info("OderManagementBtn is click")

    # ��ѡ���ŵꡱ��ť
    def choose_shop(self):
        shop_btn = self.wait_find_element(*self.shop_btn_element)
        shop_btn.click()
        # print('��ʼ����')
        # sleep(5)
        # self.swipe_up(450, 1500, 450, 1200)
        shop_name = self.wait_find_element(*self.test_shop_element)
        shop_name.click()
        logger.info("ChooseShopBtn is click")

    # ���½���������ť
    def new_oder_btn(self):
        new_oder_btn = self.wait_find_element(*self.new_oder_btn_element)
        new_oder_btn.click()
        logger.info("NewOderBtn is click")

    # ѡ�񷿼�
    def choose_room(self):
        choose_room = self.wait_find_element(*self.choose_room_element)
        # print(choose_room)
        choose_room.click()
        room_name = self.wait_find_element(*self.test_room_element)
        # print(room_name)
        room_name.click()
        logger.info("ChooseRoom is click")

    # ��ס��ʼʱ��
    def checkin_time(self):
        checkin_time = self.wait_find_element(*self.checkin_time_element)
        checkin_time.click()
        self.wait_find_element(*self.time_confirm_element).click()
        logger.info("checkin_time is click")

    # ��ס����ʱ��
    def checkout_time(self):
        checkout_time = self.wait_find_element(*self.checkout_time_element)
        checkout_time.click()
        self.wait_find_element(*self.time_confirm_element).click()
        logger.info("checkin_time is click")

    # ����ס���������ı�����
    def tenant_name(self, tenant_name_value):
        tenant_name_text = self.wait_find_element(*self.tenant_name_element)  # ������������
        tenant_name_text.click()
        AdbShell.input_text(tenant_name_value)
        # print("��ס��������",tenant_name_value)
        # tenant_name_text.send_keys(tenant_name_value)
        logger.info("TenantNameText is setValues!")


    # ����ס���ֻ��š��ı�����
    def tenant_mobile(self, tenant_mobile_value):
        tenant_mobile_text = self.wait_find_element(*self.tenant_mobile_element)  # ������������
        tenant_mobile_text.click()
        AdbShell.input_text(tenant_mobile_value)
        logger.info("TenantMobileText is setValues!")


    # �ύ����ʱ�ġ�ȷ������ť
    def confirm_button(self):
        ConfirmBtn = self.wait_find_element(*self.confirm_element)
        ConfirmBtn.click()
        logger.info("ConfirmBtn is click")

    # �½���������
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
            return "�½������ɹ�"
        except:
            print("�½�����ʧ��")
            self.get_screeShot()



if __name__ == '__main__':
    driver = desired()
    App = LoginPage(driver)
    App.login()
    YunLock_new_order = NewOderPage(driver)
    YunLock_new_order.new_order()