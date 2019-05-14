import os
import time

import pyautogui

import action


class Base(object):
    task = None
    sleep_time = 0
    screen_force = True

    def __init__(self, task, time):
        self.task = task
        self.sleep_time = time

    def work(self, name, times):
        result = self.task.shibie(name, times, self.screen_force)
        if result:
            self.cb(result)
            time.sleep(self.sleep_time)
            return True
        return False

    def touch(self, pts):
        for pt in pts:
            x, y = pt
            if self.task.is_background:
                a = "adb shell input touchscreen tap {0} {1}".format(x, y)
                os.system(a)
            else:
                x, y = int(x/2), int(y/2)
                pyautogui.click()
            # action.wait(0.15, 0.3)

    def cb(self, pt):
        pass
