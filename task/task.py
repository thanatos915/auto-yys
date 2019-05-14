import os
import time

from PIL import ImageGrab
from cv2 import cv2

import action


class Task(object):
    is_background = False

    imgs = False
    _screen = None

    def __init__(self, bg = False):
        self.imgs = action.load_imgs()
        self.is_background = bg

    def screen(self, force):
        # 后台截图
        if force or self._screen is None:
            if self.is_background:
                # pass
                a = "adb shell screencap -p sdcard/screen.jpg"
                b = "adb pull sdcard/screen.jpg"
                for row in [a, b]:
                    time.sleep(0.5)
                    os.system(row)
            else:
                screen = ImageGrab.grab()
                screen = screen.convert('RGB')
                screen.save('screen.jpg')
            screen = cv2.imread('screen.jpg')

            # 截屏，并裁剪以加速
            upleft = (0, 0)
            downright = (2550, 1400)  # 上部并排

            a, b = upleft
            c, d = downright
            screen = screen[b:d, a:c]
            self._screen = screen
            print('屏幕截图完成：', time.ctime())
        return self._screen


    def shibie(self, name, times, force = True):
        i = 1
        while times == 0 or i <= times:
            screen = self.screen(force)
            want = self.imgs[name]
            size = want[0].shape
            h, w = size
            target = screen
            pts = action.locate(target, want, 0)
            result = []
            if not len(pts) == 0:
                for pt in pts:
                    # 减去数值
                    pt = action.cheat(pt, w, h)
                    result.append(pt)
                    print("\r" + name + ' is clicked')
                return result

            i += 1
            # time.sleep(0.6)
        print("\r" + name + ' is not found')
        return False

