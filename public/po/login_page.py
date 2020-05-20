from selenium.webdriver.common.by import By
from public.po.base_view import BaseView
import logging
from log.log import logger
from public.common.desired_caps import desired
from public.common.do_excel import ReadExcel
from public.common.adb_shell import AdbShell

# 日志类的实例化
logger = logger(__name__, Cmdlevel=logging.INFO, Filelevel=logging.INFO)


class LoginPage(BaseView):
    mobile_text_element = (By.CLASS_NAME, "android.widget.EditText")
    code_text_element = (By.XPATH, "//*[contains(text(), 输入验证码)]")
    login_btn_element = (By.XPATH, "//*[@text='登录']")
    server_url = "http://127.0.0.1:4723/wd/hub"

    def __init__(self, driver):
        super().__init__(driver)

    # 手机号文本区域
    def mobile_set_text(self, mobileValue):
        mobile_text = self.wait_find_element(*self.mobile_text_element)
        # print("MobileText", MobileText.text)
        mobile_text.click()
        try:
            AdbShell.input_text(mobileValue)
            # MobileText.send_keys(mobileValue)
            logger.info("MobileText is setValues!")
        except:
            logger.info("手机号输入失败!")

    # 验证码文本区域
    def code_set_text(self, CodeValue):
        code_text = self.wait_find_element(*self.code_text_element)
        # print("MobileText", CodeText.text)
        code_text.click()
        try:
            AdbShell.input_text(CodeValue)
            # MobileText.send_keys(mobileValue)
            logger.info("CodeText is setValues!")
        except:
            logger.info("验证码输入失败!")

    # 登录按钮
    def login_button(self):
        LoginBtn = self.wait_find_element(*self.login_btn_element)
        LoginBtn.click()
        logger.info("LoginBtn is click")

    # 登录
    def login(self):
        try:
            self.wait_activity(".MainActivity", 30)
            mobileValue = int(ReadExcel("Login.xlsx", "Sheet1").read_excel(1, 0))
            codeValue = int(ReadExcel("Login.xlsx", "Sheet1").read_excel(2, 0))
            # print(mobileValue)
            # print(codeValue)
            self.mobile_set_text(mobileValue)
            self.code_set_text(codeValue)
            self.login_button()
        except:
            print("登录失败")
            self.get_screeShot()


# 调试
if __name__ == '__main__':
    driver = desired()
    Login = LoginPage(driver)
    Login.login()
    import time
    time.sleep(5)
    Login.swipe_up(0.5, 0.75, 0.5, 0.52)
    time.sleep(5)
    Login.swipe_up(0.5, 0.52, 0.5, 0.75)
