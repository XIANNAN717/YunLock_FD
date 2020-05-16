import pytest
import os
from public.po.new_room_page import NewRoomPage


class TestNewRoom():
    @pytest.mark.run(order=2)
    def test_new_room(self,app_login):
        self.room = NewRoomPage(app_login)
        self.room.wait_activity(".MainActivity", 60)
        msg = self.room.new_room()
        print(msg)
        assert '新建房源成功' == msg


# if __name__ == '__main__':
#     pytest.main(['-sq', '--alluredir', '../report/temp'])
#     # 把json文件生成测试报告
#     os.system('allure generate ../report/temp -o ../report/test_report/  --clean')

if __name__ == '__main__':
    pytest.main(['-sq', __file__, '../report/temp'])
    # 把json文件生成测试报告
    os.system('allure generate ../report/temp -o ../report/test_report/  --clean')

