# 刷宝
import time
import os
import random


class ARShaFa(object):
    def __init__(self, execount, readtime):
        self.execount = execount
        self.readtime = readtime

    def read(self, devices, screenWH):
        # 打开种子
        for dName in devices:
            os.system("adb -s %s shell am start -n com.sohu.youju/.app.ui.activity.HelloActivity" % dName)
        # # 等待
        time.sleep(30)

        count = 0
        i = 1
        # 主程序逻辑 执行时长小于总时长
        while count < self.execount:
            count += 1
            print("沙发 读了%d次" % count)
            # 随机数转换
            i = -i
            # 获取新的阅读时长
            rt = self.readtime + random.randint(1, 5)
            # # 点击第一个观看
            x1 = 100 + random.randint(0, 50) * i
            y1 = 500 - random.randint(0, 40) * i
            for dName in devices:
                os.system("adb -s " + dName + " shell input tap %d %d" % (x1, y1))
            # # 浏览70秒
            # # 记录开始时间
            start = time.time()
            # 持续固定时长X
            while (time.time() - start) < rt:
                time.sleep(3)

            n = 0
            # 设备循环执行
            for dName in devices:
                x1 = random.randint(10, 100)
                x2 = x1
                y_1_4 = screenWH[n][1] / 4
                y_3_4 = screenWH[n][1] / 4 * 3
                y1 = y_3_4 - random.randint(1, 50)
                y2 = y_1_4 - random.randint(1, 50)
                tm = 2000
                # 竟然会不定期向下翻页。。。啥情况 先翻到最上面再刷新
                os.system("adb -s " + dName + " shell input swipe %d %d %d %d %d" % (x1, y2, x2, y1, 100))

                # 下拉刷新
                os.system("adb -s " + dName + " shell input swipe %d %d %d %d %d" % (x1, y2, x2, y1, tm))
                n = n + 1


        # 等待
        # time.sleep(random.randint(1, 3))

        print("阅读完成：沙发")
        # 关闭
        for dName in devices:
            os.system("adb -s %s shell am force-stop com.sohu.youju" % dName)
