import pytest
import os
from public.po.new_order_page import NewOderPage


class TestNewOrder():
    @pytest.mark.run(order=3)
    def test_new_room(self,app_login):
        self.order = NewOderPage(app_login)
        self.order.wait_activity(".MainActivity", 60)
        msg = self.order.new_order()
        print(msg)
        assert '新建订单成功' == msg


# if __name__ == '__main__':
#     pytest.main(['-sq', '--alluredir', '../report/temp'])
#     # 把json文件生成测试报告
#     os.system('allure generate ../report/temp -o ../report/test_report/  --clean')

if __name__ == '__main__':
    pytest.main(['-sq', __file__, '../report/temp'])
    # 把json文件生成测试报告
    os.system('allure generate ../report/temp -o ../report/test_report/  --clean')
