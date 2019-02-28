# 聚看点刷阅读
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
# # 二值化
# ret, imgThreshold = cv2.threshold(imgSrc, 238, 255, cv2.THRESH_BINARY)
# 创建对比度增强图片
# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.int32)  #
# imgStrong = cv2.filter2D(imgSrc, -1, kernel)
# 转灰度，计算图片宽高
# imgGray = cv2.cvtColor(imgStrong, cv2.COLOR_BGR2GRAY)
# w_screen, h_screen = imgGray.shape[::-1]

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

# # 浏览时间
# seeTime = 30 * 4
# # 当前时间
# current = 0
# # 下滑次数
# downTicks = 3
# # 当前点击项
# currentClick = 0
# # 检索图
# imgSearch1 = cv2.imread("jukandian/search_food.jpg", 0)
# imgSearch2 = cv2.imread("jukandian/search_food_small.jpg", 0)
# # 阅读全文按钮
# imgSearchAll = cv2.imread("jukandian/search_all_click.jpg", 0)
#
# def findsearch():
#     exeCount = 0
#     # 查找 检索图 位置
#     while True:
#         if exeCount > 10:
#             print("搜索不到")
#             exit()
#         # 截图
#         os.system("adb shell screencap -p /sdcard/screen.jpg")
#         # 推送 到当前目录下
#         os.system("adb pull /sdcard/screen.jpg %s" % (os.path.abspath('.')))
#         # 读取灰度图
#         imgGray = cv2.imread("screen.jpg", 0)
#         # 匹配1号模板 美食 918
#         rightx = 918
#         res = cv2.matchTemplate(imgGray, imgSearch1, cv2.TM_SQDIFF_NORMED)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#         if (min_loc[0] > (rightx - 5)) & (min_loc[0] < (rightx + 5)):
#             # 在屏幕内
#             return min_loc[0], min_loc[1]
#         # 匹配2号模板 美食 窄 975
#         rightx = 975
#         res = cv2.matchTemplate(imgGray, imgSearch2, cv2.TM_SQDIFF_NORMED)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#         if (min_loc[0] > (rightx - 5)) & (min_loc[0] < (rightx + 5)):
#             # 在屏幕内
#             return min_loc[0], min_loc[1]
#         # 不在,向上滑动2/3屏幕，重新检索
#         os.system("adb shell input swipe 600 840 600 1700 500")  # 按住滑动
#
# def findallclick():
#     exeCount = 0
#     upordown = 1
#     # 查找 检索图 位置
#     while True:
#         if exeCount > 10:
#             print("搜索不到")
#             exit()
#         # 截图
#         os.system("adb shell screencap -p /sdcard/screen.jpg")
#         # 推送 到当前目录下
#         os.system("adb pull /sdcard/screen.jpg %s" % (os.path.abspath('.')))
#         # 读取灰度图
#         imgGray = cv2.imread("screen.jpg", 0)
#         # 匹配 阅读全文按钮
#         rightx = 514
#         res = cv2.matchTemplate(imgGray, imgSearchAll, cv2.TM_SQDIFF_NORMED)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#         if (min_loc[0] > (rightx - 5)) & (min_loc[0] < (rightx + 5)):
#             # 在屏幕内
#             return min_loc[0], min_loc[1]
#         # 不在,向上滑动屏幕，重新检索
#         os.system("adb shell input swipe 600 0 600 2000 100")  # 按住滑动
#         # 向下滑动
#         os.system("adb shell input swipe 600 800 600 0 400")  # 按住滑动


# # 主程序逻辑
# while True:
#     # 记录开始时间
#     start = time.time()
#     # 点开全文 获得更多
#     os.system("adb shell input swipe 600 800 600 0 400")  # 按住滑动
#     # 检索阅读全文按钮
#     allx, ally = findallclick()
#     # 点开阅读全文
#     os.system("adb shell input tap %d %d" % (allx, ally))
#     # 每间隔1s循环向下/向上翻页，持续固定时长X
#     while (current - start) < seeTime:
#         x = random.randint(0, 100)
#         os.system("adb shell input swipe 600 600 600 %d 400" % (500 - x))  # 按住滑动
#         current = time.time()
#         time.sleep(1)
#     # 快速向下滑动几秒 直到底
#     i = 0
#     while downTicks != i:
#         i += 1
#         os.system("adb shell input swipe 600 2000 600 0 100")  # 按住滑动
#     # 查找检索图位置
#     x, y = findsearch()
#     # 打印一下
#     print("检索到目标位置: %d   %d" % (x, y))
#     # 如果在屏幕下半部分 向上滑动500 慢慢的
#     # if y < 1000:
#     #     os.system("adb shell input swipe 600 800 600 1300 1000")  # 按住滑动
#     #     # 再获取一遍位置
#     #     x, y = findsearch()
#     #     # 打印一下
#     #     print("检索到目标位置: %d   %d" % (x, y))
#     # 点击 下一个文章的相对位置 文章item高度280
#     os.system("adb shell input tap %d %d" % (x, y))

class ARJuKanDian(object):
    # 下滑次数
    downTicks = 3
    # 检索图
    imgSearch1 = cv2.imread("jukandian/search_food.jpg", 0)
    imgSearch2 = cv2.imread("jukandian/search_food_small.jpg", 0)
    # 阅读全文按钮
    imgSearchAll = cv2.imread("jukandian/search_all_click.jpg", 0)

    def __init__(self, apptime, readtime):
        self.apptime = apptime
        self.readtime = readtime

    # 分析search.jpg位置
    def findsearch(self):
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
            # 匹配1号模板 美食 918
            rightx = 918
            res = cv2.matchTemplate(imgGray, self.imgSearch1, cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if (min_loc[0] > (rightx - 5)) & (min_loc[0] < (rightx + 5)):
                # 在屏幕内
                return min_loc[0], min_loc[1]
            # 匹配2号模板 美食 窄 975
            rightx = 975
            res = cv2.matchTemplate(imgGray, self.imgSearch2, cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if (min_loc[0] > (rightx - 5)) & (min_loc[0] < (rightx + 5)):
                # 在屏幕内
                return min_loc[0], min_loc[1]
            # 不在,向上滑动2/3屏幕，重新检索
            os.system("adb shell input swipe 600 840 600 1700 500")  # 按住滑动

    def findallclick(self):
        exeCount = 0
        upordown = 1
        # 查找 检索图 位置
        while True:
            if exeCount > 3:
                print("搜索不到")
                break
            # 截图
            os.system("adb shell screencap -p /sdcard/screen.jpg")
            # 推送 到当前目录下
            os.system("adb pull /sdcard/screen.jpg %s" % (os.path.abspath('.')))
            # 读取灰度图
            imgGray = cv2.imread("screen.jpg", 0)
            # 匹配 阅读全文按钮
            rightx = 514
            res = cv2.matchTemplate(imgGray, self.imgSearchAll, cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if (min_loc[0] > (rightx - 5)) & (min_loc[0] < (rightx + 5)):
                # 在屏幕内
                return min_loc[0], min_loc[1]
            # 不在,向上滑动屏幕，重新检索
            os.system("adb shell input swipe 600 0 600 2000 100")  # 按住滑动
            # 向下滑动
            os.system("adb shell input swipe 600 800 600 0 400")  # 按住滑动

    def read(self):
        appstart = time.time()
        # 主程序逻辑 执行时长小于总时长
        while time.time() - appstart < self.apptime:
            # 记录开始时间
            start = time.time()
            # 点开全文 获得更多
            os.system("adb shell input swipe 600 800 600 0 400")  # 按住滑动
            # 检索阅读全文按钮
            allx, ally = self.findallclick()
            # 点开阅读全文
            os.system("adb shell input tap %d %d" % (allx, ally))
            # 每间隔1s循环向下/向上翻页，持续固定时长X
            while (time.time() - start) < self.readtime:
                x = random.randint(0, 100)
                os.system("adb shell input swipe 600 600 600 %d 400" % (500 - x))  # 按住滑动
                time.sleep(1)
            # 快速向下滑动几秒 直到底
            i = 0
            while self.downTicks != i:
                i += 1
                os.system("adb shell input swipe 600 2000 600 0 100")  # 按住滑动
            # 查找检索图位置
            x, y = self.findsearch()
            # 打印一下
            print("检索到目标位置: %d   %d" % (x, y))
            # 点击 下一个文章的相对位置 文章item高度280
            os.system("adb shell input tap %d %d" % (x, y))
        print("阅读完成：聚看点")
