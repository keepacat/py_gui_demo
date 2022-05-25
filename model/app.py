import sys
import time

import torch
import numpy as np
from numba import vectorize

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QFile, QIODevice, QByteArray, QPoint

ARC_TO_DEG = 57.29577951308238
DEG_TO_ARC = 0.0174532925199433

def calPoints(arr, param):
    points = []
    for i in range(len(arr)):
        point = np.multiply(arr[i], param)
        x = np.sum(point[0])
        y = np.sum(point[1])
        points.append([x, y])
    return points

def readObj():
    file = QFile('./base.obj')
    file.open(QIODevice.ReadOnly)
    data = file.readAll()
    file.close()

    points = []
    bt = QByteArray()
    bt.append('v ')

    lines = data.split('\n')
    for line in lines:
        if line.startsWith(bt):
            line = line.simplified()
            data = line.split(' ')
            if len(data) == 4:
                point = [data[1].toFloat()[0],
                        data[2].toFloat()[0],
                        data[3].toFloat()[0]]
                points.append(point)
    return points

class Widget(QWidget):
    def __init__(self, points):
        super(Widget, self).__init__()
        self.points = points
        self.offset = QPoint(0, 0)
        self.loction = QPoint(0, 0)
        self.scaling = 10.0

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.scaling += 1.0
        else:
            self.scaling -= (1.0, 0.0)[self.scaling < 1.0]
        self.repaint()
        return super().wheelEvent(event)

    def mousePressEvent(self, event):
        self.loction = event.pos() - self.offset
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.offset = event.pos() - self.loction
        self.repaint()
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        return super().mouseReleaseEvent(event)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(QColor(0, 0, 0), 1)
        qp.setPen(pen)
        
        ox = self.offset.y() * np.pi / 180
        oy = self.offset.x() * np.pi / 180
        oz = 0

        print('paint')
        tm = time.time()

        paramx = np.array([[1, 0, 0],[0, np.cos(ox), -np.sin(ox)],[0, np.sin(ox), np.cos(ox)]])
        paramy = np.array([[np.cos(oy), 0, np.sin(oy)],[0, 1, 0],[-np.sin(oy), 0, np.cos(oy)]])
        paramz = np.array([[np.cos(oz), -np.sin(oz), 0],[np.sin(oz), np.cos(oz), 0],[0, 0, 1]])

        param = paramz * paramy * paramx
        points = calPoints(np.array(self.points), paramy)

        print(time.time() - tm)
        tm = time.time()

        for i in range(len(points)):
            x = points[i][0] * self.scaling + self.width() / 2
            y = -points[i][1] * self.scaling + self.height() * 3 / 4
            qp.drawPoint(x, y)
        qp.end()

        print(time.time() - tm)
        tm = time.time()

        return super().paintEvent(event)

app = QApplication(sys.argv)
win = Widget(readObj())
win.show()
sys.exit(app.exec())