from selenium.webdriver.common.by import By
from public.po.base_view import BaseView
import logging
from log.log import logger
from public.common.desired_caps import desired
from public.po.login_page import LoginPage
from public.common.do_excel import ReadExcel
from public.common.adb_shell import AdbShell

# 日志类的实例化
logger = logger(__name__, Cmdlevel=logging.INFO, Filelevel=logging.INFO)

class RegisterPage(BaseView):
    id_card_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]"
    name_text_element = (By.CLASS_NAME, "android.widget.EditText")
    id_card_text_element = (By.XPATH, id_card_xpath)
    next_btn_element = (By.XPATH, "//*[@text='下一步']")
    server_url = "http://127.0.0.1:4723/wd/hub"

    def __init__(self, driver):
        super().__init__(driver)

    # 姓名文本区域
    def name_text(self, name_value):
        name_text = self.wait_find_element(*self.name_text_element)
        # print("MobileText", MobileText.text)
        name_text.click()
        try:
            AdbShell.input_text(name_value)
            # MobileText.send_keys(mobileValue)
            logger.info("name_text is setValues!")
            self.get_screeShot()
        except:
            logger.info("姓名输入失败!")

    # 身份证号文本区域
    def id_card_text(self, id_card_value):
        id_card_text = self.wait_find_element(*self.id_card_text_element)
        # print("MobileText", CodeText.text)
        id_card_text.click()
        try:
            AdbShell.input_text(id_card_value)
            logger.info("id_card_text is setValues!")
            self.get_screeShot()
        except:
            logger.info("验证码输入失败!")

    # 下一步按钮
    def next_btn(self):
        next_btn = self.wait_find_element(*self.next_btn_element)
        next_btn.click()
        logger.info("next_btn is click")

    # 注册流程
    def register(self):
        try:
            self.wait_activity(".MainActivity", 30)
            name_value = ReadExcel("register.xlsx", "Sheet1").read_excel(1, 0)
            id_card_value = int(ReadExcel("register.xlsx", "Sheet1").read_excel(1, 1))
            self.name_text(name_value)
            self.id_card_text(id_card_value)
            self.next_btn()
            return "注册成功"
        except:
            print("注册失败")


# 调试
if __name__ == '__main__':
    driver = desired()
    Login = LoginPage(driver)
    Login.login()
    register = RegisterPage(driver)
    register.register()
