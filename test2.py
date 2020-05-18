from public.common.desired_caps import desired
from public.po.login_page import LoginPage
from selenium.webdriver.common.by import By
from public.po.base_view import BaseView
from time import sleep

driver = desired()
#
def login():
    login = LoginPage(driver)
    login.login()
    return login
#
def lock():
    l = login()
    count_num = 10000  #
    actual_count_num = 0  #
    succ_num = 0  #
    for t in range(count_num):
        actual_count_num += 1
        try:
            lock_list_01_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button[2]"
            # lock_list_02_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Button[2]"
            unlock_01_text = l.find_element(By.XPATH, lock_list_01_xpath)
            # unlock_02_text = base.find_element(By.XPATH, lock_list_02_xpath)
            unlock_01_text.click()
            # sleep(10)
            # unlock_02_text.click()
            succ_num += 1
            print("123".format(succ_num))
            sleep(20)
        except:
            sleep(10)
            login()


lock_test = lock()