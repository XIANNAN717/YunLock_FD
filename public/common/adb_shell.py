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
