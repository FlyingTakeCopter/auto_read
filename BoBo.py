# 刷宝
import time
import os
import random


class ARBoBo(object):
    def __init__(self, execount, readtime):
        self.execount = execount
        self.readtime = readtime

    def read(self, devices):
        count = 0
        i = 1
        # 主程序逻辑 执行时长小于总时长
        while count < self.execount:
            count += 1
            # 随机数转换
            i = -i
            # 获取新的阅读时长
            rt = self.readtime + random.randint(1, 5) * i
            # 点击第一个观看
            x1 = 600 + random.randint(0, 100) * i
            y1 = 400 - random.randint(0, 40) * i
            for dName in devices:
                os.system("adb -s " + dName + " shell input tap %d %d" % (x1, y1))
            # 浏览70秒
            # 记录开始时间
            start = time.time()
            # 持续固定时长X
            while (time.time() - start) < rt:
                time.sleep(3)
            # 设备循环执行
            for dName in devices:
                x1 = random.randint(300, 350)
                x2 = x1 + random.randint(0, 5) * i
                y1 = 900 + random.randint(0, 50) * i
                y2 = 300 + random.randint(0, 50) * i
                tm = random.randint(400, 1000)
                # 下拉刷新
                os.system("adb -s " + dName + " shell input swipe %d %d %d %d %d" % (x1, y2, x2, y1, tm))
                # 等待
                time.sleep(random.randint(1, 4))

        print("阅读完成：波波")
