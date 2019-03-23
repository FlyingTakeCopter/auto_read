# 刷宝
import time
import os
import random


class ARHuiShiPin(object):
    def __init__(self, execount, readtime):
        self.execount = execount
        self.readtime = readtime

    def read(self, devices, screenWH):
        # 打开
        for dName in devices:
            os.system("adb -s %s shell am start -n com.cashvideo/.LaunchPageActivity" % dName)
        # 等待
        time.sleep(30)

        count = 0
        # 主程序逻辑 执行时长小于总时长
        while count < self.execount:
            count += 1
            print("种子 读了%d次" % count)
            # 随机数转换
            # 获取新的阅读时长
            rt = self.readtime + random.randint(1, 5)
            # 点击第一个观看
            x1 = random.randint(10, 100)
            y1 = 700 - random.randint(0, 40)
            for dName in devices:
                os.system("adb -s " + dName + " shell input tap %d %d &" % (x1, y1))
            # 记录开始时间
            start = time.time()
            # 持续固定时长X
            while (time.time() - start) < rt:
                time.sleep(3)

            # 点击领取金币 每个视频看40秒 没两个视频领一次奖励
            if count > 2 & ((count % 2) == 0):
                n = 0
                for dName in devices:
                    os.system("adb -s %s shell input tap %d %d &" % (dName, screenWH[n][0] - 100, screenWH[n][1] - 100))
                    n = n + 1

            for dName in devices:
                os.system("adb -s " + dName + " shell input keyevent 4")
                os.system("adb -s " + dName + " shell input keyevent 4")
            # time.sleep(1)
            # 设备循环执行
            for dName in devices:
                # os.system("adb -s " + dName + " shell input keyevent 4")
                # time.sleep(1)
                x1 = random.randint(100, 150)
                x2 = x1
                y1 = 900 + random.randint(0, 10)
                y2 = y1 - random.randint(500, 550)
                tm = 1000
                # 下拉刷新
                os.system("adb -s " + dName + " shell input swipe %d %d %d %d %d &" % (x1, y2, x2, y1, tm))
            # 等待
            # time.sleep(random.randint(1, 3))

        print("阅读完成：惠视频")
        # 关闭
        for dName in devices:
            os.system("adb -s %s shell am force-stop com.cashvideo" % dName)

