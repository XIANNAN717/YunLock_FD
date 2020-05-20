import os


class AdbShell():
    @staticmethod
    def input_text(text):
        """
        :param text: 输入的文本
        :return:
        """
        result = os.system('adb shell input text {}'.format(str(text)))
        return result
    @staticmethod
    def screen():
        os.system('adb shell screencap -p /sdcard/screen.png')  # 获取当前手机切图
        os.system('adb pull /sdcard/screen.png')  # 把当前这个切图上传到本地目录