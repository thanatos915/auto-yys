import time
import traceback

import pyautogui

import action
from task.down import Down
from task.task import Task
from task.tiaozhan import Tiaozhan
from task.zhunbei import Zhunbei

pyautogui.PAUSE = 0.1

task = Task()
tasks = []
start_time = time.time()

print('程序启动，现在时间', time.ctime())

def log(f):
    def wrap(*agrs, **kwagrs):
        try:
            ans = f(*agrs, **kwagrs)
            return ans
        except:
            traceback.print_exc()
            time.sleep(60)

    return wrap


@log
def select_mode():
    print('''\n菜单：  鼠标移动到最右侧中止并返回菜单页面, 
        1 单刷
        2 后台单刷
        ''')

    raw = input("选择功能模式：")
    index = int(raw)

    mode = [0, dan]
    comand = mode[index]
    comand()
    run()

def run():
    while True:
        for task in tasks:
            result = task.do()
            # print("\r" + result)

def dan():
    #初始化 Task
    tasks.append(Tiaozhan(task, 0))
    tasks.append(Zhunbei(task, 24))
    tasks.append(Down(task, 1))


if __name__ == '__main__':
    select_mode()