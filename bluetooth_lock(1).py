"""
自动化开锁实现需求（5把门锁）：
1、点击开锁后，等待20S，滑动，再次点击“立即开锁”
2、若点击“立即开锁”第一个元素失败，则点击第二个元素，注意：点击第二个元素时，不用再设置超时
3、若报错“连接失败”，等待点击“确定”按钮
# 4、若页面任何元素找不到，则点击“我的”，再点击“门锁管理”，达到刷新的目的（没有刷新成功）
5、当全部门锁依次点击开锁完毕后（滑动计数来判断是否滑到底部），重新登录（因为向下滑操作不成功），滑动计数归置为0

"""

from public.common.desired_caps import desired
from public.po.base_view import BaseView
from selenium.webdriver.common.by import By
from log.log import logger
import logging
from time import sleep

logger = logger(__name__, Cmdlevel=logging.INFO, Filelevel=logging.INFO)
class UnLock():
    def __init__(self):
        pass

    # 打开APP
    def open_app(self):
        self.swipe_num = 0
        driver = desired()
        base = BaseView(driver)
        return base

    # 等待第一个元素（立即开锁）出现
    def wait_unlock_click(self,num):
        lock_list_01_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[{num}]/android.view.View/android.widget.Button[2]".format(num=str(num))
        unlock_01_text = self.l.wait_find_element(By.XPATH, lock_list_01_xpath)
        unlock_01_text.click()

    # 第二个元素（立即开锁）不用等待，直接点击
    def unlock_click(self,num):
        lock_list_01_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[{num}]/android.view.View/android.widget.Button[2]".format(num=str(num))
        unlock_01_text = self.l.find_element(By.XPATH, lock_list_01_xpath)
        unlock_01_text.click()

    # 开锁方法
    def on_lock(self,t):
        print("第{}次点击开锁".format(t))
        try:
            try:
                self.wait_unlock_click(1)
                sleep(30)
            except:
                self.unlock_click(2)
                sleep(30)
            # 判断开锁是否成功,开锁失败点击确定重新点击开锁
            try:
                confirm_text =  self.l.find_element(By.XPATH, "//*[@text='确定']")
                confirm_text.click()
                if t%4 != 0:
                    logger.info("第{}把门锁开锁失败".format(t % 4))
                else:
                    logger.info("第4把门锁开锁失败")
                return t%4

            #开锁成功按照正常流程进行
            except:
                if t%4 != 0:
                    logger.info("第{}把门锁开锁成功".format(t%4))
                else:
                    logger.info("第4把门锁开锁成功")
                # print("第{}把门锁开锁成功".format(succ_num))
                self.l.swipe_up(0.5, 0.75, 0.5, 0.42)
                # 每滑动一次，就在原来的基础上+1
                self.swipe_num +=1
                print(("第{}次滑动").format(self.swipe_num))
                # 滑动到第5次时，就点击手机屏幕上第二个“立即开锁”按钮
                if self.swipe_num==5:
                    self.unlock_click(1)
                    sleep(30)
                    # 向下滑,门锁列表回到最顶部
                    print("开始向下滑")
                    self.l.swipe_down()
                    self.swipe_num = 0
                return t

        except Exception as e:
            print("异常信息",e)
            try:
                confirm_text =  self.l.wait_find_element(By.XPATH, "//*[@text='确定']")
                confirm_text.click()
            except:
                # self.l = self.open_app()
                # t = 1
                # self.swipe_num = 0
                self.lock()
            # return t

    # 循环开锁
    def lock(self):
        self.l = self.open_app()
        count_num = 10000  #  设定的开锁总数统计
        for t in range(1,count_num):
            self.on_lock(t)



lock_test = UnLock()
lock_test.lock()







