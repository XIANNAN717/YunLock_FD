import pytest
import os
from public.po.new_shop_page import NewShopPage


class TestNewShop():
    @pytest.mark.run(order=1)
    def test_new_shop(self,app_login):
        self.shop = NewShopPage(app_login)
        self.shop.wait_activity(".MainActivity", 60)
        msg = self.shop.new_shop()
        print(msg)
        assert '新建门店成功' == msg


# if __name__ == '__main__':
#     pytest.main(['-sq', '--alluredir', '../report/temp'])
#     # 把json文件生成测试报告
#     os.system('allure generate ../report/temp -o ../report/test_report/  --clean')

if __name__ == '__main__':
    pytest.main(['-sq', __file__, '../report/temp'])
    # 把json文件生成测试报告
    os.system('allure generate ../report/temp -o ../report/test_report/  --clean')