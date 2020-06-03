# coding=utf-8
import aircv as ac
import os


class CustomError(Exception):
    """

    """

    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


class PictureRecognition(object):

    # 获取对应的图片的坐标点
    @classmethod
    def matchImg(cls, imgobj, imgsrc='screen.png', confidence=0.5):
        """

        :param imgobj: 需要操作的图片
        :param imgsrc: 整个页面的图片
        :param confidence: 默认匹配率（设定为50%，超过50%才匹配，低于50%。返回None）
        :return:
        """
        imsrc = ac.imread(imgsrc)
        imobj = ac.imread(imgobj)
        match_result = ac.find_template(imsrc, imobj, confidence)
        # 可看到图片匹配率
        # print(match_result)
        os.remove(imgsrc)
        # match_result为None或不为None时满足自定义条件
        if not match_result or match_result and match_result['confidence'] < 0.99:
            imgobj_name = imgobj.split('data/images/')[1]
            raise CustomError(imgobj_name + '图片识别失败')
        else:
            x = match_result['result'][0]
            y = match_result['result'][1]
            # 当前 x y 为识别图片的中心点，可以进行直接点击
            return x, y


if __name__ == '__main__':

    fd = PictureRecognition.matchImg(r'F:\YunLock_FD\data\images\entrance\FD.png',
                                    r'F:\YunLock_FD\public\po\e28e216e-a597-11ea-b4ba-28e347f84a0fscreen_all.png')

    fk = PictureRecognition.matchImg(r'F:\YunLock_FD\data\images\entrance\FK.png',
                                    r'F:\YunLock_FD\public\po\e28e216e-a597-11ea-b4ba-28e347f84a0fscreen_all.png')


    print(fd)
    print(fk)
