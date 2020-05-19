import pytest
import os
from public.po.temporary_authorization_page import TemporaryAuthorization



class TestTemporaryAuthorization():
    @pytest.mark.run(order=5)
    def test_TemporaryAuthorization(self,app_login):
        self.TemporaryAuthorization = TemporaryAuthorization(app_login)
        self.TemporaryAuthorization.wait_activity(".MainActivity", 60)
        msg = self.TemporaryAuthorization.temporary_authorization_process()
        print(msg)
        assert '临时授权成功' == msg


# if __name__ == '__main__':
#     pytest.main(['-sq', '--alluredir', '../report/temp'])
#     # 把json文件生成测试报告
#     os.system('allure generate ../report/temp -o ../report/test_report/  --clean')

if __name__ == '__main__':
    pytest.main(['-sq', __file__, '../report/temp'])
    # 把json文件生成测试报告
    os.system('allure generate ../report/temp -o ../report/test_report/  --clean')