class TestCaseInfo():
    """
    测试用例信息
    """

    def __init__(self,id="",name="",owner="",starttime="",endtime="",secondsDuration="",erroninfo=""):
        self.id = id
        self.name = name
        self.owner = owner
        self.starttime = starttime
        self.endtime = endtime
        self.secondsDuration= secondsDuration
        self.errorinfo = erroninfo


