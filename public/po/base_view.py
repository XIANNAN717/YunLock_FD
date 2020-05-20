from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import global_config


img_path = global_config.Images_path

class BaseView():
    def __init__(self,driver):
        self.driver = driver

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
            return WebDriverWait(self.driver,40).until(EC.visibility_of_element_located(loc))
        except:
            try:
                return self.driver.find_element(*loc)
            except:
                print("元素未找到")
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
            print("元素未找到")
            print("{}该activity中未找到{}元素".format(self, loc))
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
        s = self.driver.get_window_size()
        print(s)
        x1 = start_width  # 起点x坐标
        y1 = start_height  # 起点y坐标
        x2 = end_width  # 终点x坐标
        y2 = end_height  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y2, t)


    # 向下滑动
    def swipe_down(self, t=500, n=1):
        s = self.get_size()
        print(s)
        x1 = int(s[0] * 0.5)  # x坐标
        y1 = int(s[1] * 0.5)  # 起点y坐标
        y2 = int(s[1] * 0.8)  # 终点y坐标
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



