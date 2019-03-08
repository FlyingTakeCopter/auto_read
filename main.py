from QuTouTiao import ARQuTouTiao
from JuKanDian import ARJuKanDian
from HongBaoTouTiao import ARHongBaoTouTiao
from ShuaBao import ARShuaBao
from BoBo import ARBoBo
import os

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

# 刷宝
appTime_qtt = appTimeBase * 1.3
readTime_qtt = 10

autoShuaBao = ARShuaBao(appTime_qtt, readTime_qtt)
autoShuaBao.read(devices)

# 波波
# aRBoBo = ARBoBo(execount=100, readtime=70)
# aRBoBo.read(devices)

# 沙发视频
# aRBoBo = ARBoBo(execount=100, readtime=60)
# aRBoBo.read(devices)



