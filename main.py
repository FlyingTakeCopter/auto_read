from QuTouTiao import ARQuTouTiao
from JuKanDian import ARJuKanDian
from HongBaoTouTiao import ARHongBaoTouTiao
from ShuaBao import ARShuaBao
from BoBo import ARBoBo
from ShaFa import ARShaFa
from ZhongZi import ARZhongZi
from ZhongZi import ARZhongZiThread
from HaoKan import ARHaoKan
import os
import re
import time

# 获取模拟器总数
def getDevicesAll():
    devices = []
    try:
        for dName_ in os.popen("adb devices"):
            if "\t" in dName_:
                # 真机
                devices.append(dName_.split("\t")[0])
                # 模拟器检索
                # findres = dName_.find("emulator")
                # if findres != -1:
                #     devices.append(dName_.split("\t")[0])
        devices.sort(cmp=None, key=None, reverse=False)
    except:
        pass
    print("\n设备名称: %s \n总数量:%s台" % (devices, len(devices)))
    return devices


devices = getDevicesAll()

for dName in devices:
    # 亮屏
    os.system("adb -s %s shell input keyevent 26" % dName)
    # 开机
    os.system("adb -s %s shell input swipe 500 1200 500 100 100" % dName)

# 获取分辨率
# 获取屏幕分辨率计算屏幕中心
# f = os.popen("adb shell wm size")
# screen_width,screen_height = re.search("(\d{3,4})x(\d{3,4})", f.read()).groups()
# center = (int(screen_width)/2, int(screen_height)/2)

time.sleep(5)

# 查看前台应用
# adb shell dumpsys activity activities

# 查看电池状态
# adb shell dumpsys battery

# 查看内存
# MemTotal 就是设备的总内存，MemFree 是当前空闲内存。

# 检测设备是否已 root
# 命令：
# adb shell
# su
# 此时命令行提示符是 $ 则表示没有 root 权限，是 # 则表示已 root。

# 时间单位 1小时
appTimeBase = 3600
# 单篇阅读时长 30秒
readTimeBase = 30

"""
app名称
App阅读时长
文章阅读时长
"""
# 趣头条
# appTime_qtt = appTimeBase * 2
# readTime_qtt = readTimeBase * 2
#
# autoReadQuTouTiao = ARQuTouTiao(appTime_qtt, readTime_qtt)
# autoReadQuTouTiao.read()

# 聚看点
# appTime_qtt = appTimeBase * 3
# readTime_qtt = 40 * 3
#
# autoJuKanDian = ARJuKanDian(appTime_qtt, readTime_qtt)
# autoJuKanDian.read()

# 红包头条
# appTime_qtt = appTimeBase * 3
# readTime_qtt = 20
#
# autoHongBaoTouTiao = ARHongBaoTouTiao(appTime_qtt, readTime_qtt)
# autoHongBaoTouTiao.read()

# 刷宝 com.jm.video/.ui.main.SplashActivity
# 打开刷宝
# appTime_qtt = appTimeBase * 2
# autoShuaBao = ARShuaBao(appTime_qtt)
# autoShuaBao.read(devices)

# 波波 550706账号2分钟下发100
# tv.yixia.bobo/com.kg.v1.welcome.WelcomeActivity
aRBoBo = ARBoBo(execount=100, readtime=120)
aRBoBo.read(devices)

# 沙发视频 60s 10金币 6000 = 1元 全看完要10个小时 逗我呢？
# com.sohu.youju/.app.ui.activity.HelloActivity
# aRShaFa = ARShaFa(execount=100, readtime=3)
# aRShaFa.read(devices)

# 种子
# com.inke.gaia/.splash.SplashActivity
aRZhongZi = ARZhongZi(execount=10000, readtime=30)
aRZhongZi.read(devices)

# aRZhongZiThread = ARZhongZiThread(100, 50)
# ARZhongZiThread.read(aRZhongZiThread, devices)

# 好看
# aRHaoKan = ARHaoKan(execount=200, readtime=60)
# aRHaoKan.read(devices)



