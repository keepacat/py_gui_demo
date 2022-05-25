# coding:utf8
from tkinter import filedialog
from tkinter.messagebox import showinfo
from debugpy import connect
from requests import patch
import win32com
from win32com.client import Dispatch, constants
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from reportlab.lib.units import cm
from zmq import NULL


def getWordAddWatermark(content):
    wordApp = win32com.client.DispatchEx("Word.Application")  # 打开word进程
    wordApp.Visible = True
    wordApp.DisplayAlerts = False
    doc = wordApp.Documents.Open(content['path'])

    actDoc = wordApp.ActiveDocument
    Sect = actDoc.Sections(1).Range.Select()
    wordApp.ActiveWindow.ActivePane.View.SeekView = 9
    # selectObj = wordApp.Selection

    wordApp.Selection.HeaderFooter.Shapes.AddTextEffect(content['effect'], content['text'], content['font'], content['size'], False, False, 0, 0).Select()
    # wordApp.Selection.ShapeRange.Name = '0'

    wordApp.Selection.ShapeRange.TextEffect.NormalizedHeight = False
    wordApp.Selection.ShapeRange.Line.Visible = False
    wordApp.Selection.ShapeRange.Fill.Visible = True
    wordApp.Selection.ShapeRange.Fill.Solid
    wordApp.Selection.ShapeRange.Fill.ForeColor = 0
    wordApp.Selection.ShapeRange.Fill.Transparency = 0.5
    # 设置颜色
    wordApp.Selection.ShapeRange.Fill.ForeColor.ObjectThemeColor = 14
    wordApp.Selection.ShapeRange.Fill.ForeColor.TintAndShade = 0
    wordApp.Selection.ShapeRange.Rotation = 315
    wordApp.Selection.ShapeRange.LockAspectRatio = True
    wordApp.Selection.ShapeRange.Height = 120
    wordApp.Selection.ShapeRange.Width = 460
    wordApp.Selection.ShapeRange.WrapFormat.AllowOverlap = True
    # wordApp.Selection.ShapeRange.WrapFormat.Side = wdWrapNone
    wordApp.Selection.ShapeRange.WrapFormat.Type = 3
    wordApp.Selection.ShapeRange.WrapFormat.Side = 3
    wordApp.Selection.ShapeRange.RelativeVerticalPosition = 0
    wordApp.Selection.ShapeRange.Left = -999995
    wordApp.Selection.ShapeRange.Top = -999995

    # 关闭页眉页脚
    wordApp.ActiveWindow.ActivePane.View.SeekView = 0
    actDoc.Save()
    actDoc.Close()
    wordApp.Quit()

app = QApplication(sys.argv)

paths = QFileDialog.getOpenFileNames(None, 'Open file','','*.docx')[0]
if len(paths) > 0:
    vlayout = QVBoxLayout()

    label = QLabel('水印内容：')
    text = QLineEdit('小林通')
    hlayout = QHBoxLayout()
    hlayout.addWidget(label)
    hlayout.addWidget(text)
    vlayout.addLayout(hlayout)

    label = QLabel('字体风格：')
    effect = QSpinBox()
    effect.setValue(0)
    hlayout = QHBoxLayout()
    hlayout.addWidget(label)
    hlayout.addWidget(effect)
    vlayout.addLayout(hlayout)

    label = QLabel('字体名称：')
    font = QLineEdit('等线')
    hlayout = QHBoxLayout()
    hlayout.addWidget(label)
    hlayout.addWidget(font)
    vlayout.addLayout(hlayout)

    label = QLabel('字体大小：')
    size = QSpinBox()
    size.setValue(1)
    hlayout = QHBoxLayout()
    hlayout.addWidget(label)
    hlayout.addWidget(size)
    vlayout.addLayout(hlayout)

    button1 = QPushButton('确定')
    button2 = QPushButton('取消')
    hlayout = QHBoxLayout()
    hlayout.addWidget(button1)
    hlayout.addWidget(button2)
    vlayout.addLayout(hlayout)

    win = QDialog()
    win.setWindowTitle('添加水印')
    win.resize(300, 400)
    win.setLayout(vlayout)

    button1.clicked.connect(win.accept)
    button2.clicked.connect(win.reject)
    if win.exec_() == QDialog.Accepted:
        for path in paths:
            content = { 
                'path' :  path,
                'text' :  text.text(),
                'effect' :  effect.value(),
                'font' :  font.text(),
                'size' :  size.value() 
            }
            getWordAddWatermark(content)
        QMessageBox.about(None, '提示', '水印添加完成')

# sys.exit(app.exec_())

