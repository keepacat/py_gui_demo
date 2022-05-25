from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from you_get import common as you_get

import os
print(os.system('you-get -i http://www.bilibili.com/video/av9581328/'))
# p = os.popen('you-get -i http://www.bilibili.com/video/av9581328/')
# info = p.read()
# print("p.read():\n", info)

# app = QApplication([])
# player = QMediaPlayer()
# wgt_video = QVideoWidget()  # 视频显示的widget
# wgt_video.show()
# player.setVideoOutput(wgt_video)  # 视频输出的widget
# player.setMedia(QMediaContent(QUrl("D:\\video.flv")))  # 选取视频文件
# player.play()
# app.exec_()