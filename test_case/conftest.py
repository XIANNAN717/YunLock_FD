import pytest
import allure
from public.common.desired_caps import desired
from public.po.login_page import LoginPage


"""
pytest里面固定的conftest.py名称是用来做前置步骤的
这个文件时在运行用例的时候会自动去找这个文件里面的前置步骤方法执行的
"""

@pytest.fixture(scope='session')
def app_login():
    """
    @pytest.fixture()的scope参数有四个值：
    scope='function'
    函数级别的fixture每个测试函数 只运行一次。配置代码在测试用例运行之前运行，销毁代码在测试用例运行之后执行。function是fixture参数的默认值。
    scope='class'
    类级别的fixture每个测试类只运行一次，不管测试类中有多少个类方法都可以共享这个fixture
    scope='module'
    模块级别的fixture每个模块只运行一次，不管模块里有多少个测试函数，类方法或其他fixture都可以共享这个fixture
    scope='session'
    会话级别的fixture每次会话只运行一次。一次pytest会话中的所有测试函数、方法都可以共享这个fixture

    :return:
    """
    print('登陆')
    with allure.step('登陆'):#给报告里面加步骤提示
        driver = desired()
        App = LoginPage(driver)
        App.login()
    yield driver
    driver.close_app()
    print("\n关闭应用")
