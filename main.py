from QuTouTiao import ARQuTouTiao
from JuKanDian import ARJuKanDian

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
appTime_qtt = appTimeBase * 1
readTime_qtt = readTimeBase * 2

# autoReadQuTouTiao = ARQuTouTiao(appTime_qtt, readTime_qtt)
# autoReadQuTouTiao.read()

# 聚看点
appTime_qtt = appTimeBase * 1
readTime_qtt = readTimeBase * 3

autoJuKanDian = ARJuKanDian(appTime_qtt, readTime_qtt)
autoJuKanDian.read()