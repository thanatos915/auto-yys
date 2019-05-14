import os
import random

import action
from task.base import Base

class Down(Base):
    p_pt = None

    def do(self):
        return self.work('shuju', 30)

    def cb(self, pts):
        for pt in pts:
            w, h = pt
            # print(w, h)
            for x in range(1, 5):
                click = [(w + random.randint(-10, 15) , h + random.randint(100, 300))]
                print(click)
                self.touch(click)
                action.wait(0.8, 1.1)
