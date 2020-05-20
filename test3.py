from public.common.desired_caps import desired
from public.po.login_page import LoginPage
from selenium.webdriver.common.by import By
from time import sleep


class UnLock():
    def __init__(self):
        self.l = None
        self.swipe_num = 0
    # 登录
    def login(self):
        self.swipe_num = 0
        driver = desired()
        L = LoginPage(driver)
        L.login()
        # login.swipe_up()
        sleep(3)
        return L

    def re_f5(self):
        pass

    def wait_unlock_click(self,num):
        lock_list_01_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[{num}]/android.view.View/android.widget.Button[2]".format(num=str(num))
        unlock_01_text = self.l.wait_find_element(By.XPATH, lock_list_01_xpath)
        unlock_01_text.click()
    def unlock_click(self,num):
        lock_list_01_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[{num}]/android.view.View/android.widget.Button[2]".format(num=str(num))
        unlock_01_text = self.l.find_element(By.XPATH, lock_list_01_xpath)
        unlock_01_text.click()

    def on_lock(self,succ_num):
        try:
            try:
                self.wait_unlock_click(1)
                sleep(10)
            except:
                sleep(10)
                self.unlock_click(2)
            #尝试滑动,滑动失败就再次尝试滑动，滑动成功
            self.l.swipe_up(0.5, 0.75, 0.5, 0.52)
            self.swipe_num +=1
            if self.swipe_num==5:
                self.unlock_click(2)
            if self.swipe_num==6:
                self.unlock_click(3)
                print("返回到房源列表顶部")
                # for i in range(3):
                #     self.l.swipe_up(0.5, 0.52, 0.5, 0.75)
                self.login()
                self.swipe_num = 0
            succ_num += 1
            print("第{}次成功开锁".format(succ_num))
            return succ_num
        except:
            try:
                confirm_text =  self.l.find_element(By.XPATH, "//*[@text='确定']")
                confirm_text.click()
            except:
                sleep(10)
                try:
                    self.re_f5()
                except:
                    self.l =self.login()


    def lock(self):
        self.l = self.login()
        count_num = 10000  #  设定的开锁总数统计
        actual_count_num = 0  # 实际开锁总数统计
        succ_num = 0  # 开锁成功次数
        for t in range(count_num):
            actual_count_num += 1
            succ_num = self.on_lock(succ_num)



lock_test = UnLock()
lock_test.lock()

