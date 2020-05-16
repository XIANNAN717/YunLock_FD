import pytest
import os
from public.po.artificial_authentication_page import ArtificialAuthenticationPage


class TestArtificialAuthentication():
    @pytest.mark.run(order=4)
    def test_artificial_authentication(self,app_login):
        self.ArtificialAuthentication = ArtificialAuthenticationPage(app_login)
        self.ArtificialAuthentication.wait_activity(".MainActivity", 60)
        msg = self.ArtificialAuthentication.artificial_authentication_Process()
        print(msg)
        assert '人工认证成功' == msg


# if __name__ == '__main__':
#     pytest.main(['-sq', '--alluredir', '../report/temp'])
#     # 把json文件生成测试报告
#     os.system('allure generate ../report/temp -o ../report/test_report/  --clean')

if __name__ == '__main__':
    pytest.main(['-sq', __file__, '../report/temp'])
    # 把json文件生成测试报告
    os.system('allure generate ../report/temp -o ../report/test_report/  --clean')
