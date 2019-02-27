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


class AutoReadQuTouTiao(object):
    # 浏览时间
    seeTime = 30 * 4
    # 当前时间
    current = 0
    # 下滑次数
    downTicks = 3
    # 当前点击项
    currentClick = 0
    # 检索图
    imgSearch3 = cv2.imread("search3.jpg", 0)
    imgSearch4 = cv2.imread("search4.jpg", 0)
    imgSearch5 = cv2.imread("search5.jpg", 0)
    imgSearch6 = cv2.imread("search6.jpg", 0)

    # 分析search.jpg位置
    @classmethod
    def findsearch(cls):
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
            # 二值化
            # ret, imgThreshold = cv2.threshold(imgGray, 250, 255, cv2.THRESH_BINARY)
            # 模板匹配，检测坐标
            # 匹配3号模板 imgSearch3 570
            # res = cv2.matchTemplate(imgGray, imgSearch3, cv2.TM_SQDIFF_NORMED)
            # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            # if (min_loc[0] > 565) & (min_loc[0] < 575):
            #     # 在屏幕内
            #     return min_loc[0], min_loc[1]
            # 匹配4号模板 imgSearch4 564
            # res = cv2.matchTemplate(imgGray, imgSearch4, cv2.TM_SQDIFF_NORMED)
            # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            # if (min_loc[0] > 559) & (min_loc[0] < 569):
            #     # 在屏幕内
            #     return min_loc[0], min_loc[1]
            # 匹配5号模板 深色广告 imgSearch5 927
            res = cv2.matchTemplate(imgGray, cls.imgSearch5, cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if (min_loc[0] > 922) & (min_loc[0] < 932):
                # 在屏幕内
                return min_loc[0], min_loc[1]
            # 匹配6号模板 浅色广告 imgSearch5 957
            res = cv2.matchTemplate(imgGray, cls.imgSearch6, cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if (min_loc[0] > 952) & (min_loc[0] < 962):
                # 在屏幕内
                return min_loc[0], min_loc[1]
            # 不在,向上滑动2/3屏幕，重新检索
            os.system("adb shell input swipe 600 840 600 1700 500")  # 按住滑动

    @classmethod
    def run(cls):
        # 主程序逻辑
        while True:
            # 记录开始时间
            start = time.time()
            # 每间隔1s循环向下/向上翻页，持续固定时长X
            while (current - start) < cls.seeTime:
                x = random.randint(0, 100)
                os.system("adb shell input swipe 600 600 600 %d 400" % (500 - x))  # 按住滑动
                current = time.time()
                time.sleep(1)
            # 快速向下滑动几秒 直到底
            i = 0
            while cls.downTicks != i:
                i += 1
                os.system("adb shell input swipe 600 2000 600 0 100")  # 按住滑动
            # 查找检索图位置
            x, y = cls.findsearch()
            # 打印一下
            print("检索到目标位置: %d   %d" % (x, y))
            # 如果在屏幕下半部分 向上滑动500 慢慢的
            if y > 1000:
                os.system("adb shell input swipe 600 1300 600 800 1000")  # 按住滑动
                # 再获取一遍位置
                x, y = cls.findsearch()
                # 打印一下
                print("检索到目标位置: %d   %d" % (x, y))

            # 这块不完善
            # 假设没有评论的话，如果没拖动说检索错误了,被最底下的广告影响了
            if y > 1800:
                # 向上盲点一下，先暂时这样
                # 点击 下一个文章的相对位置 文章item高度280
                os.system("adb shell input tap 600 %d" % (y - 1200))
            else:
                # 高度自身偏移85 计算广告item底边高度
                y += 85
                # 点击 下一个文章的相对位置 文章item高度280
                os.system("adb shell input tap 600 %d" % (y + 280 / 2))