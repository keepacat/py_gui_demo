#-*- coding: UTF-8 -*-
from PIL import Image
from flask import Flask, make_response, render_template
import os
import random

filterSize = (278, 192)
filterPath = os.path.split(__file__)[0] + '/images/'
filterFiles = []

app = Flask(__name__)

@app.route('/images/<name>',methods = ['POST', 'GET'])
def images(name):
    path = filterPath + name
    if ~os.path.exists(path):
        name = filterFiles[random.randint(0, filterFiles.__len__() - 1)]
    image = open(filterPath + name, 'rb').read()
    response = make_response(image)
    response.headers['Content-Type'] = 'image/jpg'
    return response


# 遍历指定目录，显示目录下的所有文件名
def filterFile(filepath):
    dirs =  os.listdir(filepath)
    for allDir in dirs:
        path = os.path.join('%s/%s' % (filepath, allDir))
        image = Image.open(path)
        if image.size > filterSize:
            x = 0
            y = 0
            img = image.crop((x, y, x + filterSize[0], y + filterSize[1]))
            img.save(filterPath + allDir)
    return dirs

filterFiles.extend(filterFile('./排球少年'))
filterFiles.extend(filterFile('./排球少年2'))
filterFiles.extend(filterFile('./排球少年3'))

app.run(host="0.0.0.0", port=8080)