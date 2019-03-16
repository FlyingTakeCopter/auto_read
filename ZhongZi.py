# 刷宝
import time
import os
import random
import _thread


class ARZhongZi(object):
    def __init__(self, execount, readtime):
        self.execount = execount
        self.readtime = readtime

    def read(self, devices):
        # 打开种子
        for dName in devices:
            os.system("adb -s %s shell am start -n com.inke.gaia/.splash.SplashActivity" % dName)
        # 等待
        time.sleep(30)

        count = 0
        i = 1
        # 主程序逻辑 执行时长小于总时长
        while count < self.execount:
            count += 1
            print("种子 读了%d次" % count)
            # 随机数转换
            i = -i
            # 获取新的阅读时长
            rt = self.readtime + random.randint(1, 5)
            # 点击第一个观看
            x1 = 600 + random.randint(0, 100) * i
            y1 = 500 - random.randint(0, 40) * i
            for dName in devices:
                os.system("adb -s " + dName + " shell input tap %d %d &" % (x1, y1))
            # 浏览70秒
            # 记录开始时间
            start = time.time()
            # 持续固定时长X
            while (time.time() - start) < rt:
                time.sleep(3)
            for dName in devices:
                os.system("adb -s " + dName + " shell input keyevent 4")
                # os.system("adb -s " + dName + " shell input keyevent 4")
            # time.sleep(1)
            # 设备循环执行
            for dName in devices:
                # os.system("adb -s " + dName + " shell input keyevent 4")
                # time.sleep(1)
                x1 = random.randint(300, 350)
                x2 = x1
                y1 = 900 + random.randint(0, 10)
                y2 = y1 - random.randint(500, 550)
                tm = 1000
                # 下拉刷新
                os.system("adb -s " + dName + " shell input swipe %d %d %d %d %d &" % (x1, y2, x2, y1, tm))
            # 等待
            # time.sleep(random.randint(1, 3))

        print("阅读完成：种子")
        # 关闭
        for dName in devices:
            os.system("adb -s %s shell am force-stop com.inke.gaia", dName)


class ARZhongZiThread(object):
    def __init__(self, execount, readtime):
        self.execount = execount
        self.readtime = readtime

    def read(self, devices):
        try:
            for dName in devices:
                _thread.start_new_thread(readthread, (self.execount, dName, self.readtime))
        except:
            print("线程异常")
        pass


def readthread(execount, dName, readtime):
    count = 0
    i = 1
    # 主程序逻辑 执行时长小于总时长
    while count < execount:
        count += 1
        print("种子 读了%d次" % count)
        # 随机数转换
        i = -i
        # 获取新的阅读时长
        rt = readtime + random.randint(1, 5)
        # 点击第一个观看
        x1 = 600 + random.randint(0, 100) * i
        y1 = 500 - random.randint(0, 40) * i
        os.system("adb -s " + dName + " shell input tap %d %d &" % (x1, y1))
        # 浏览70秒
        # 记录开始时间
        start = time.time()
        # 持续固定时长X
        while (time.time() - start) < rt:
            time.sleep(3)
        # 设备循环执行
        os.system("adb -s " + dName + " shell input keyevent 4")
        time.sleep(1)
        x1 = random.randint(300, 350)
        x2 = x1
        y1 = 900 + random.randint(0, 10)
        y2 = y1 - random.randint(500, 550)
        tm = 1000
        # 下拉刷新
        os.system("adb -s " + dName + " shell input swipe %d %d %d %d %d &" % (x1, y2, x2, y1, tm))
        # 等待
        # time.sleep(random.randint(1, 3))
