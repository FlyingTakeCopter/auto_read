# 刷宝
import time
import os


class ARShuaBao(object):
    def __init__(self, apptime, readtime):
        self.apptime = apptime
        self.readtime = readtime

    def read(self, devices):
        appstart = time.time()
        # 主程序逻辑 执行时长小于总时长
        while (time.time() - appstart) < self.apptime:
            # 浏览20秒
            # 记录开始时间
            start = time.time()
            # 每间隔1s循环向下/向上翻页，持续固定时长X
            while (time.time() - start) < self.readtime:
                time.sleep(10)
            # 设备循环执行
            for dName in devices:
                os.system("adb -s " + dName + " shell input swipe 300 800 300 200 100")  # 后台执行 小米800-200
        print("阅读完成：刷宝")
