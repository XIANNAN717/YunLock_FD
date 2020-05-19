from public.common.desired_caps import desired
from public.po.login_page import LoginPage
from selenium.webdriver.common.by import By
from time import sleep


# 登录
def login():
    driver = desired()
    login = LoginPage(driver)
    login.login()
    return login
#
def lock():
    l = login()
    count_num = 10000  #  设定的开锁总数统计
    actual_count_num = 0  # 实际开锁总数统计
    succ_num = 0  # 开锁成功次数
    for t in range(count_num):
        actual_count_num += 1
        try:
            # lock_list_01_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button[2]"
            lock_list_02_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Button[2]"
            # unlock_01_text = l.find_element(By.XPATH, lock_list_01_xpath)
            unlock_02_text = l.find_element(By.XPATH, lock_list_02_xpath)
            # unlock_01_text.click()
            # sleep(10)
            unlock_02_text.click()
            succ_num += 1
            print("第{}次成功开锁".format(succ_num))
            sleep(20)
        except:
            login()


lock_test = lock()