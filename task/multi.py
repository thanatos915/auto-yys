import os
import random
import time

import pyautogui

from task.base import Base
from task.down import Down


class Multi(Base):
    name = ''

    game_time = 0

    action = None

    _down = None

    _down_two = None

    # 标签位置
    tabs = [
        (310, 42),
        (400, 40)
    ]

    def __init__(self, task, name, time):
        Base.__init__(self, task, 0)
        self.game_time = time
        self.name = name

    def start(self):
        self.action = 'kaishi'
        self.work('kaishi', 5)

    def down(self):
        if (self._down is None):
            down = Down(self.task, 0)
            self._down = down
        return self._down

    # def down_two(self):
    #     if (self._down_two is None):
    #         down = Down(self.task, 0)
    #         self._down_two = down
    #     return self._down_two


    def do(self):
        os.system("adb shell am start com.netease.onmyoji.netease_simulator/com.netease.onmyoji.Launcher")
        # pyautogui.click(self.tabs[0])
        self.start()
        print('执行结束')
        self.down().do()
        # pyautogui.click(self.tabs[1])
        os.system("adb shell am start com.netease.onmyoji.netease_simulator.p71bHrVo_1/com.netease.onmyoji.Launcher")
        self.down().cb(self.down().p_pt)
        # self.down_two().do()
        print('执行结束')


    def cb(self, pt):
        if self.action == 'kaishi':
            self.touch(pt)
            if self.name == '11':
                self.tag()
            else:
                time.sleep(self.game_time)

    def tag(self):
        start = int(time.time())
        time.sleep(1.5)
        while (start + self.game_time - 8) > int(time.time()):
            click = [(random.randint(710, 730), random.randint(150, 180))]
            self.touch(click)
            print('我标记了：', click)
            time.sleep(0.8)
