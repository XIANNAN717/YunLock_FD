from public.po.login_page import LoginPage
from public.common.do_excel import ReadExcel
from public.common.desired_caps import desired


mobileValue = int(ReadExcel("Login.xlsx", "Sheet1").read_excel(1, 0))

class TestLogin():
    def setUp(self):
        self.driver = desired()

    def test_login(self):
        self.login = LoginPage(self.driver)
        self.login.wait_activity(".MainActivity",60)
        self.login.login()

    def tearDown(self):
        self.driver.close_app()



