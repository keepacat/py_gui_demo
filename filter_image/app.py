#-*- coding: UTF-8 -*-
from PIL import Image
import os

filterSize = (300, 300)
filterPath = './image/'

# 遍历指定目录，显示目录下的所有文件名
def filterFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        path = os.path.join('%s/%s' % (filepath, allDir))
        image = Image.open(path)
        if image.size > filterSize:
            x = 0
            y = 0
            img = image.crop((x, y, x + filterSize[0], y + filterSize[1]))
            img.save(filterPath + allDir)


filterFile('./排球少年')
# filterFile('./排球少年2')
# filterFile('./排球少年3')