import pyautogui

from task.base import Base

class Agree(Base):
    is_auto = False
    jieshou_times = 0

    def need(self):
        return self.is_auto == False and self.jieshou_times >= 2

    def do(self):
        if self.is_auto == False:
            result = self.work('jieshou2', 5)
            if result:
                self.is_auto = True
                return '自动接受'

        if self.jieshou_times < 2:
            self.jieshou_times += 1
            result = self.work('jieshou', 5)
            if result:
                return '接受组队'

        return '没有组队邀请'

    def cb(self, pt):
        # pass
        pyautogui.click(pt)

