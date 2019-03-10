# 刷宝
import time
import os
import random


class ARShuaBao(object):
    def __init__(self, apptime):
        self.apptime = apptime

    def read(self, devices):
        appstart = time.time()
        count = 0
        # 主程序逻辑 执行时长小于总时长
        while (time.time() - appstart) < self.apptime:
            count += 1
            print("阅读%d次" % count)
            # 随机阅读时间
            readtime = random.randint(3, 6)
            # 记录开始时间
            start = time.time()
            # 每间隔1s循环向下/向上翻页，持续固定时长X
            while (time.time() - start) < readtime:
                time.sleep(3)

            x = random.randint(350, 450)
            y1 = random.randint(800, 850)
            y2 = y1 - random.randint(600, 610)
            # 设备循环执行
            for dName in devices:
                os.system("adb -s " + dName + " shell input swipe %d %d %d %d 1500 &" % (x, y1, x, y2))  # 后台执行 小米800-200
        print("阅读完成：刷宝")
