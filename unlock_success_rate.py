from public.common.desired_caps import desired
from public.po.login_page import LoginPage
from selenium.webdriver.common.by import By
from public.po.base_view import BaseView
from time import sleep


driver = desired()
Login = LoginPage(driver)
base = BaseView(driver)


count_num = 1000  # 设定的开锁总数统计
actual_count_num = 0  # 实际开锁总数统计
succ_num = 0  # 开锁成功次数
fail_num = 0  # 开锁失败次数

for t in range(count_num):
    actual_count_num += 1
    try:
        unlock_text = base.find_element(By.XPATH, "//*[@text='立即开锁']")
        unlock_text.click()
        succ_num += 1
        print("第{}次成功开锁".format(succ_num))
        sleep(30)
    except:
        sleep(5)
        # confirm_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button"
        # confirm_btn = base.find_element(By.XPATH, confirm_btn_xpath)
        confirm_btn = base.find_element(By.XPATH, "//*[@text='确定']")
        confirm_btn.click()
        print("点击‘确定’成功")
        sleep(5)
        unlock_text = base.find_element(By.XPATH, "//*[@text='立即开锁']")
        unlock_text.click()
        fail_num += 1
        print("第{}次开锁失败".format(fail_num))
        sleep(30)
    finally:
        print("设定开锁统计：", count_num)
        print("实际开锁统计：", actual_count_num)
        print("成功开锁统计：",succ_num)
        print("失败开锁统计：",fail_num)
        # 开锁成功率
        succ_rate = '开锁成功率：{:.2%}'.format(succ_num/actual_count_num)
        fail_rate = '开锁失败率：{:.2%}'.format(fail_num/actual_count_num)
        print(succ_rate)
        print(fail_rate)
        print("=" * 35)
