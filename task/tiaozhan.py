import time

import pyautogui

from task.base import Base

class Tiaozhan(Base):

    # screen_force = False

    def do(self):
        return self.work('tiaozhan', 1)

    def cb(self, pt):
        print(pt)
        self.touch(pt)
            # pyautogui.click(pt)
        # pass
        # pyautogui.click(pt)

