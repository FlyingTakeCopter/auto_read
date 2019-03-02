# 趣头条刷阅读
import cv2
import time
import os
import random
from sys import exit

# os.system("adb shell screencap -p /sdcard/screen.jpg")
# # 推送 到当前目录下
# os.system("adb pull /sdcard/screen.jpg %s" % (os.path.abspath('.')))
# # 截图保存到的临时路径
# imgSrc = cv2.imread("screen.jpg", 0)

# 查找检索图位置
# x, y = findsearch()
# 打印一下
# print("%d   %d" % (x, y))

# 显示图片
# imgShow = cv2.pyrDown(imgSrc)
# imgShow = imgSrc
# cv2.namedWindow("show")
# cv2.imshow("show", imgShow)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 浏览时间
seeTime = 20
# 当前时间
current = 0
# 下滑次数
downTicks = 3
# 当前点击项
currentClick = 0
# 检索图
imgSearch = cv2.imread("hongbaotoutiao/search_ad.jpg", 0)
imgSearch2 = cv2.imread("hongbaotoutiao/search_ad2.jpg", 0)

#
def findsearch():
    exeCount = 0
    # 查找 检索图 位置
    while True:
        if exeCount > 10:
            print("搜索不到")
            exit()
        # 截图
        os.system("adb shell screencap -p /sdcard/screen.jpg")
        # 推送 到当前目录下
        os.system("adb pull /sdcard/screen.jpg %s" % (os.path.abspath('.')))
        # 读取灰度图
        imgGray = cv2.imread("screen.jpg", 0)
        # 匹配模板 广告 imgSearch 32
        rightx = 32
        res = cv2.matchTemplate(imgGray, imgSearch, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if (min_loc[0] > (rightx - 5)) & (min_loc[0] < (rightx + 5)):
            # 在屏幕内
            return min_loc[0], min_loc[1]
        # 匹配模板 广告 imgSearch2 64
        rightx = 64
        res = cv2.matchTemplate(imgGray, imgSearch2, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if (min_loc[0] > (rightx - 5)) & (min_loc[0] < (rightx + 5)):
            # 在屏幕内
            return min_loc[0], min_loc[1]
        # 不在,向上滑动2/3屏幕，重新检索
        os.system("adb shell input swipe 600 1700 600 840 500")  # 按住滑动


# 主程序逻辑
while True:
    # 找广告坐标
    x, y = findsearch()
    # 没找到广告坐标 说明本页面
    while True:
        # 在屏幕下半部分，滚动到屏幕上半部分
        if y > 1500:
            os.system("adb shell input swipe 600 1700 600 700 500")  # 向上滑动
        elif y > 1000:
            os.system("adb shell input swipe 600 1200 600 800 500")  # 向上滑动
        elif y > 500:
            os.system("adb shell input swipe 600 1000 600 800 500")  # 向上滑动
        else:
            break
        # 再获取一遍位置
        x, y = findsearch()
    # 点进广告下方第一篇文章
    os.system("adb shell input tap 600 %d" % (y + 300))
    # 浏览25秒
    # 记录开始时间
    start = time.time()
    # 每间隔1s循环向下/向上翻页，持续固定时长X
    while (time.time() - start) < seeTime:
        x = random.randint(0, 100)
        os.system("adb shell input swipe 600 1600 600 %d 400" % (1500 - x))  # 慢慢向上滑动
        time.sleep(0.5)
    # 退出
    os.system("adb shell input tap 87 157 ")
    # 向下滚动
    os.system("adb shell input swipe 600 1200 750 %d 400" % (500 - x))  # 按住滑动

# class ARQuTouTiao(object):
#     # 下滑次数
#     downTicks = 3
#     # 检索图
#     # imgSearch3 = cv2.imread("search3.jpg", 0)
#     # imgSearch4 = cv2.imread("search4.jpg", 0)
#     imgSearch5 = cv2.imread("search5.jpg", 0)
#     imgSearch6 = cv2.imread("search6.jpg", 0)
#
#     def __init__(self, apptime, readtime):
#         self.apptime = apptime
#         self.readtime = readtime
#
#     # 分析search.jpg位置
#     def findsearch(self):
#         execount = 0
#         # 查找 检索图 位置
#         while True:
#             if execount > 10:
#                 print("搜索不到")
#                 exit()
#             # 截图
#             os.system("adb shell screencap -p /sdcard/screen.jpg")
#             # 推送 到当前目录下
#             os.system("adb pull /sdcard/screen.jpg %s" % (os.path.abspath('.')))
#             # 读取灰度图
#             imggray = cv2.imread("screen.jpg", 0)
#             # 二值化
#             # ret, imgThreshold = cv2.threshold(imgGray, 250, 255, cv2.THRESH_BINARY)
#             # 模板匹配，检测坐标
#             # 匹配3号模板 imgSearch3 570
#             # res = cv2.matchTemplate(imgGray, imgSearch3, cv2.TM_SQDIFF_NORMED)
#             # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#             # if (min_loc[0] > 565) & (min_loc[0] < 575):
#             #     # 在屏幕内
#             #     return min_loc[0], min_loc[1]
#             # 匹配4号模板 imgSearch4 564
#             # res = cv2.matchTemplate(imgGray, imgSearch4, cv2.TM_SQDIFF_NORMED)
#             # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#             # if (min_loc[0] > 559) & (min_loc[0] < 569):
#             #     # 在屏幕内
#             #     return min_loc[0], min_loc[1]
#             # 匹配5号模板 深色广告 imgSearch5 927
#             res = cv2.matchTemplate(imggray, self.imgSearch5, cv2.TM_SQDIFF_NORMED)
#             min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#             if (min_loc[0] > 922) & (min_loc[0] < 932):
#                 # 在屏幕内
#                 return min_loc[0], min_loc[1]
#             # 匹配6号模板 浅色广告 imgSearch5 957
#             res = cv2.matchTemplate(imggray, self.imgSearch6, cv2.TM_SQDIFF_NORMED)
#             min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#             if (min_loc[0] > 952) & (min_loc[0] < 962):
#                 # 在屏幕内
#                 return min_loc[0], min_loc[1]
#             # 不在,向上滑动2/3屏幕，重新检索
#             os.system("adb shell input swipe 600 840 600 1700 500")  # 按住滑动
#
#     def read(self):
#         appstart = time.time()
#         # 主程序逻辑 执行时长小于总时长
#         while (time.time() - appstart) < self.apptime:
#             # 记录开始时间
#             readstart = time.time()
#             # 每间隔1s循环向下/向上翻页，持续固定时长X
#             while (time.time() - readstart) < self.readtime:
#                 x = random.randint(0, 100)
#                 os.system("adb shell input swipe 600 600 600 %d 400" % (500 - x))  # 按住滑动
#                 time.sleep(0.5)
#             # 快速向下滑动几秒 直到底
#             i = 0
#             while self.downTicks != i:
#                 i += 1
#                 os.system("adb shell input swipe 600 2000 600 0 100")  # 按住滑动
#             # 查找检索图位置
#             x, y = self.findsearch()
#             # 打印一下
#             print("检索到目标位置: %d   %d" % (x, y))
#             # 如果在屏幕下半部分 向上滑动500 慢慢的
#             if y > 1000:
#                 os.system("adb shell input swipe 600 1300 600 800 1000")  # 按住滑动
#                 # 再获取一遍位置
#                 x, y = self.findsearch()
#                 # 打印一下
#                 print("检索到目标位置: %d   %d" % (x, y))
#
#             # 这块不完善
#             # 假设没有评论的话，如果没拖动说检索错误了,被最底下的广告影响了
#             if y > 1800:
#                 # 向上盲点一下，先暂时这样
#                 # 点击 下一个文章的相对位置 文章item高度280
#                 os.system("adb shell input tap 600 %d" % (y - 1200))
#             else:
#                 # 高度自身偏移85 计算广告item底边高度
#                 y += 85
#                 # 点击 下一个文章的相对位置 文章item高度280
#                 os.system("adb shell input tap 600 %d" % (y + 280 / 2))
#         print("阅读完成：趣头条")
