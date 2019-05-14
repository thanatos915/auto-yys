import time

import pyautogui

from task.base import Base

class Zhunbei(Base):

    action = 'check_lock'
    check_lock = False
    is_lock = False
    screen_force = False

    def do(self):
        if self.is_lock:
            time.sleep(self.sleep_time)
            return True
        # 检查是否固定
        self.action = 'check_lock'
        # self.check_lock = True
        result = self.work('lock', 1)
        if result:
            return result
        self.action = 'do_zhunbei'
        # self.check_lock = False

        # if not result:
        #     self.action = 'do_lock'
        #     result = self.work('dolock', 1)
        #     if result:
        #         return result

        if not self.is_lock:
            self.screen_force = True
            i = 1
            while i <= 4:
                result = self.work('zhunbei', 1)
                if result:
                    return result
                self.screen_force = False
                self.work('zhan', 1)
                self.screen_force = True
                i+=1
                # time.sleep(0.5)

    def cb(self, pt):
        if self.action != 'check_lock':
            # pass
            self.touch(pt)
            # pyautogui.click(pt)
        else:
            self.is_lock = True
