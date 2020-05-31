from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import global_config
from public.common.desired_caps import desired
import os
import allure
import uuid
from public.common.picture_recognition import PictureRecognition
img_path = global_config.Images_path


class BaseView():
    def __init__(self,driver):
        self.driver = driver
        self.image_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/data/image/'

    def wait_activity(self,waitActivity,time):
        """
        将webdriver提供的wait_activity方法进行封装
        :param waitActivity:
        :param time:
        :return:
        """
        self.driver.wait_activity(waitActivity,time)
        AC = self.driver.current_activity
        # print(AC)

        # 截图
    def get_screeShot(self):
        now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))  # 获取当前系统时间
        imageName = img_path + "\\" + now + ".png"  # 拼接截图名称
        self.driver.get_screenshot_as_file(imageName)


    # 查找元素二次封装
    def wait_find_element(self, *loc):
        """
         将webdriver中find_element进行二次封装，增加等待时间，超时抛异常
        :param loc: *loc 代表任意数量的位置参数（带单个星号的参数）
        :return:
        """
        try:
            return WebDriverWait(self.driver,60).until(EC.visibility_of_element_located(loc))
        except:
            try:
                return self.driver.find_element(*loc)
            except:
                print("{}该activity中未找到{}元素".format(self, loc))
                self.get_screeShot()
                raise (TimeoutError)

    # 查找元素二次封装
    def find_element(self, *loc):
        """
         将webdriver中find_element进行二次封装，增加等待时间，超时抛异常
        :param loc: *loc 代表任意数量的位置参数（带单个星号的参数）
        :return:
        """
        try:
            return self.driver.find_element(*loc)
        except:
            # print("{}该activity中未找到{}元素".format(self, loc))
            self.get_screeShot()
            raise (TimeoutError)

    # 获得机器屏幕大小x,y
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 向上滑动
    def unlock_swipe_up(self, t=500, n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.75  # 起点y坐标
        y2 = s['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

     # 向上滑动
    def swipe_up(self, start_width, start_height, end_width, end_height, t=1000, n=1, ):
        # s = self.driver.get_window_size()
        # print(s)
        x1 = start_width  # 起点x坐标
        y1 = start_height  # 起点y坐标
        x2 = end_width  # 终点x坐标
        y2 = end_height  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y2, t)


    # 向下滑动
    def swipe_down(self, t=300, n=2):
        s = self.get_size()
        # print(s)
        x1 = int(s[0] * 0.5)  # x坐标
        y1 = int(s[1] * 0.25)  # 起点y坐标
        y2 = int(s[1] * 0.85)  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)



    # 向左滑动
    def swipe_left(self, t=500, n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.75
        y1 = s['height'] * 0.5
        x2 = s['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)


    # 向右滑动
    def swipe_right(self,t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def touch_tap(self, x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
        '''
        method explain:点击坐标
        parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
        Usage:
            device.touch_coordinate(277,431)      #277.431为点击某个元素的x与y值
        '''
        screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        print("x1,y1",x1,y1)
        self.driver.tap([(x1, y1), (x1, y1)], duration)

    def click_img(self,img_name):
        """
        传入图片名，可点击图片。图片路径与名字不能包含中文
        :param img_name:
        :return:
        """
        with allure.step('步骤：点击图片{img_name}'.format(img_name=img_name)):
            img_name = self.image_path + img_name
            sereen_all_filename = str(uuid.uuid1())+'screen_all.png'
            self.driver.get_screenshot_as_file(sereen_all_filename)
            x,y = PictureRecognition.matchImg(img_name, sereen_all_filename)
            print('x,y',x,y)
            self.touch_tap(x,y)

if __name__ == '__main__':
    driver = desired()
    b = BaseView(driver)
    b.unlock_swipe_up()
    b.swipe_down()

