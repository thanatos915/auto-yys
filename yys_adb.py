import cv2,numpy,time,random
import os,sys,traceback
from PIL import ImageGrab
import action_adb as action

# 读取文件 精度控制   显示名字
imgs = action.load_imgs()


start_time = time.time()
print('程序启动，现在时间', time.ctime())


#以上启动，载入设置
##########################################################

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
        1 结界自动合卡，自动选择前三张合成 
        2 自动通关魂十，自动接受组队并确认通关
        3 自动通关业原火，单刷
        4 自动刷组队狗粮（打手模式），          
        5 单刷探索副本，无法区分经验BUFF
        ''')
    action.alarm(1)
    raw = input("选择功能模式：")
    index = int(raw)

    mode = [0, card, yuhun, yeyuanhuo, goliang, solo]
    comand = mode[index]
    comand()

##########################################################
#合成结界卡，较简单，未偏移直接点
def card():
    while True:            
        x, y, z = (370, 238), (384, 385), (391, 525)  #前三张卡的位置
        zz = (871, 615)               #合成按钮位置
        for i in [x, y, z ,zz]:
            pyautogui.click(i)
            time.sleep(0.1)
        time.sleep(0.5)


########################################################
#魂十通关
def yuhun():
    while True :
        screen = action.screen_shot()
        print(screen)
        # screen = cv2.imread('screen.jpg')

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (2550, 770) 
        print('screen shot ok',time.ctime())
        
        #设定目标，开始查找
        #这里是自动接受组队
        for i in ['jieshou2',"jieshou"]:
            want = imgs[i]
            size = want[0].shape
            h, w , ___ = size
            x1,x2 = upleft, (430, 358)
            target = action.cut(screen, x1, x2)
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                print('接受组队')
                xx = pts[0]
                xx = action.cheat(xx, w, h)
                if xx[0] > 120:           
                    action.touch(xx)
                    action.wait()
                    break
                else:
                    pass
                continue

        #自动点击通关结束后的页面
        for i in ['ying','jiangli','kaishi','jixu' ]:
            want = imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                for pt in pts:
                    pt = action.cheat(pt, w, h)
                    action.touch(pt)
                    action.wait(0.15, 0.3)
                break
    select_mode()

########################################################
#业原火通关
def yeyuanhuo():
    while True :   #直到取消，或者出错
        screen = action.screen_shot()
        screen = cv2.imread('screen.jpg')

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1426, 798)
        print('screen shot ok',time.ctime())
        
        #设定目标，开始查找

        #过关
        for i in ['ying','jiangli','tiaozhan','jixu']:
            want = imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                for pt in pts:
                    pt = action.cheat(pt, w, h)
                    action.touch(pt)
                    action.wait()
                break

########################################################
#狗粮通关
def goliang():
    while True:   #直到取消，或者出错
        screen = action.screen_shot()
        screen = cv2.imread('screen.jpg')

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1358, 768)
        downright2 = (2550, 768)
        print('screen shot ok',time.ctime())
        
        #设定目标，开始查找
        #进入后
        want=imgs['guding']

        x1 = (785, 606)
        x2 = downright
        target = action.cut(screen, x1, x2)
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('正在地图中')
            
            want = imgs['xiao']
            x1,x2 = (5, 405), (119, 560)
            target = action.cut(screen, x1, x2)
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                print('组队状态中')
            else:
                print('退出重新组队')
                
                for i in ['queren', 'tuichu']:
                    want = imgs[i]
                    size = want[0].shape
                    h, w , ___ = size
                    x1,x2 = upleft, (965, 522)
                    target = action.cut(screen, x1, x2)
                    pts = action.locate(target,want,0)
                    if not len(pts) == 0:
                        print('退出中')
                        try:
                            queding = pts[1]
                        except:
                            queding = pts[0]
                        queding = action.cheat(queding, w, h)
                        action.touch(queding)
                        action.wait()
                        break
                continue

        want = imgs['jieshou']
        size = want[0].shape
        h, w , ___ = size
        x1,x2 = upleft, (250, 380)
        target = action.cut(screen, x1, x2)
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('接受组队')
            xx = pts[0]
            xx = action.cheat(xx, w, h)
            if xx[0] > 120:           
                action.touch(xx)
                action.wait()
            else:
                pass
            continue

        for i in ['ying','jiangli','jixu']:
            want = imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                print('领取奖励')
                xy = action.cheat(pts[0], w, h-10 )
                action.touch(xy)
                action.wait()
                break

########################################################
#单人探索
def solo():
    while True:   #直到取消，或者出错
        screen = action.screen_shot()
        screen = cv2.imread('screen.jpg')

        #截屏，并裁剪以加速
        upleft = (0, 0)
        downright = (1358, 768)
        downright2 = (2550, 768)
        print('screen shot ok',time.ctime())
        
        #设定目标，开始查找
        #进入后
        want = imgs['guding']

        x1 = (785, 606)
        x2 = downright
        target = action.cut(screen, x1, x2)
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('正在地图中')
            
            want = imgs['left']
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                right = (854, 527)
                right = action.cheat(right, 10, 10)
                action.touch(right)
                action.wait()
                continue

            want = imgs['jian']
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                print('点击小怪')
                xx = action.cheat(pts[0], 10, 10)        
                action.touch(xx)
                time.sleep(0.5)
                continue
            else:
                for i in ['queren', 'tuichu']:
                    want = imgs[i]
                    size = want[0].shape
                    h, w , ___ = size
                    x1,x2 = upleft, (965, 522)
                    target = action.cut(screen, x1, x2)
                    pts = action.locate(target,want,0)
                    if not len(pts) == 0:
                        print('退出中')
                        try:
                            queding = pts[1]
                        except:
                            queding = pts[0]
                        queding = action.cheat(queding, w, h)
                        action.touch(queding)
                        action.wait()
                        break
                continue

        for i in ['ying','jiangli','jixu']:
            want = imgs[i]
            size = want[0].shape
            h, w , ___ = size
            target = screen
            pts = action.locate(target,want,0)
            if not len(pts) == 0:
                print('领取奖励')
                xy = action.cheat(pts[0], w, h-10 )
                action.touch(xy)
                action.wait()
                break

        want = imgs['tansuo']
        size = want[0].shape
        h, w , ___ = size
        target = screen
        pts = action.locate(target,want,0)
        if not len(pts) == 0:
            print('进入地图')
            xy = action.cheat(pts[0], w, h-10 )
            action.touch(xy)
            action.wait()

####################################################




if __name__ == '__main__':
    select_mode()

