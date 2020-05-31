import pytest
import os
from public.po.new_room_page import NewRoomPage


class TestNewRoom():
    @pytest.mark.run(order=2)
    def test_new_room(self,app_login):
        self.room = NewRoomPage(app_login)
        self.room.wait_activity(".MainActivity", 60)
        import time
        time.sleep(5)
        #点击图片
        self.room.click_img(r'your_fenzu1/quxiao.png')
        time.sleep(10)
        assert 1

if __name__ == '__main__':
    pytest.main(['-sq', __file__, '../report/temp'])
    # 把json文件生成测试报告
    #os.system('allure generate ../report/temp -o ../report/test_report/  --clean')

