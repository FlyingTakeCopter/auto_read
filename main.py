from QuTouTiao import ARQuTouTiao
from JuKanDian import ARJuKanDian
from HongBaoTouTiao import ARHongBaoTouTiao
from ShuaBao import ARShuaBao

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
appTime_qtt = appTimeBase * 3
readTime_qtt = 30

autoShuaBao = ARShuaBao(appTime_qtt, readTime_qtt)
autoShuaBao.read()
