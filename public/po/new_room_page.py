# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from public.po.base_view import BaseView
import logging
from log.log import logger
from public.common.desired_caps import desired
from public.common.do_excel import ReadExcel
from public.po.login_page import LoginPage
from public.common.adb_shell import AdbShell


# 日志类的实例化
logger = logger(__name__, Cmdlevel=logging.INFO, Filelevel=logging.INFO)

class NewRoomPage(BaseView):
    room_type_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.widget.EditText"
    room_name_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.widget.EditText"
    room_description_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[6]/android.widget.EditText"
    confirm_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button"


    room_text_element = (By.XPATH, "//*[@text='新添房源']")
    room_type_description_element = (By.XPATH, room_type_xpath)
    room_name_element = (By.XPATH, room_name_xpath)
    room_description_element = (By.XPATH, room_description_xpath)
    confirm_element = (By.XPATH, confirm_btn_xpath)


    def __init__(self,driver):
        super().__init__(driver)

    # 新添房源按钮
    def new_room_btn(self):
        new_room_Btn = self.wait_find_element(*self.room_text_element)
        try:
            new_room_Btn.click()
            logger.info("new_oder_Btn is click")
        except:
            logger.info("进入新添房源界面失败")

   # # 户型描述文本区域(坐标定位元素)
   #  def room_type(self, room_type_Value):
   #      self.driver.tap([(0, 402), (900, 576)], 500) # 户型描述输入
   #      AdbShell.input_text(room_type_Value)
   #      # room_type_text.send_keys(room_type_Value)
   #      logger.info("RoomTypeText is setValues!")
   #      self.get_screeShot()

    # 户型描述文本区域
    def room_type(self, room_type_Value):
        room_type_text = self.wait_find_element(*self.room_type_description_element)  # 户型描述输入
        room_type_text.click()
        AdbShell.input_text(room_type_Value)
        # room_type_text.send_keys(room_type_Value)
        logger.info("RoomTypeText is setValues!")
        self.get_screeShot()


    # 房源昵称文本区域
    def room_name(self, room_name_Value):
        room_name_text = self.wait_find_element(*self.room_name_element)
        # print("room_name_text", room_name_text.text)
        room_name_text.click()
        try:
            AdbShell.input_text(room_name_Value)
            # room_type_text.send_keys(room_type_Value)
            logger.info("RoomNameText is setValues!")
            self.get_screeShot()
        except:
            logger.info("房源昵称字段输入内容失败")

    # 房源介绍文本区域
    def room_description(self, room_description_Value):
        room_description_text = self.wait_find_element(*self.room_description_element)
        # print("room_description_text", room_description.text)
        room_description_text.click()
        try:
            AdbShell.input_text(room_description_Value)
            # room_type_text.send_keys(room_type_Value)
            logger.info("RoomDescriptionText is setValues!")
            self.get_screeShot()
        except:
            logger.info("房源介绍字段输入内容失败")

   # 确定按钮
    def confirm_button(self):
        ConfirmBtn = self.wait_find_element(*self.confirm_element)
        ConfirmBtn.click()
        logger.info("ConfirmBtn is click")

    # 新建订单流程
    def new_room(self):
        try:
            self.new_room_btn()
            room_type_Value = ReadExcel("new_room.xlsx", "Sheet1").read_excel(1, 0)
            room_name = ReadExcel("new_room.xlsx", "Sheet1").read_excel(1, 1)
            room_description = ReadExcel("new_room.xlsx", "Sheet1").read_excel(1, 2)
            self.room_type(room_type_Value)
            self.room_name(room_name)
            self.room_description(room_description)
            self.confirm_button()
            return "新建房源成功"
        except:
            print("新建房源失败")



if __name__ == '__main__':
    driver = desired()
    App = LoginPage(driver)
    App.login()
    YunLock_new_room = NewRoomPage(driver)
    YunLock_new_room.new_room()

