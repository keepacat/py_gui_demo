from PyPDF2 import PdfFileReader, PdfFileWriter
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    """把水印添加到pdf中"""
    pdf_output = PdfFileWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(input_stream, strict=False)

    # 获取PDF文件的页数
    pageNum = pdf_input.getNumPages()

    # 读入水印pdf文件
    pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.getPage(i)
        page.mergePage(pdf_watermark.getPage(0))
        page.compressContentStreams()  # 压缩内容
        pdf_output.addPage(page)
    pdf_output.write(open(pdf_file_out, 'wb'))

def start_watermark():
    files = QFileDialog.getOpenFileNames()[0]
    markfile = QFileDialog.getOpenFileName()[0]

    for file in files:
        pdf_file_in = file
        pdf_file_mark = markfile
        pdf_file_out = file.replace('.pdf', '_Marked.pdf')
        add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)


def button1_click(line1):
    dir = QFileDialog.getExistingDirectory()
    line1.setText(dir)


def button2_click(line2):
    file = QFileDialog.getOpenFileName()[0]
    line2.setText(file)

def button3_click(line1, line2):
    dir = line1.text()
    markfile = line2.text()
    files =  os.listdir(dir)
    for file in files:
        path = os.path.join('%s/%s' % (dir, file))

        file_out = path.replace('.pdf', '_Marked.pdf')
        add_watermark(path, markfile, file_out)
    QMessageBox.about(None, '提示', '水印添加完成')



app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle('pdf批量添加水印')
win.setMinimumWidth(400)

line1 = QLineEdit()
line2 = QLineEdit()

button1 = QPushButton('预览')
button2 = QPushButton('预览')
button3 = QPushButton('开始')

button1.clicked.connect(lambda: button1_click(line1))
button2.clicked.connect(lambda: button2_click(line2))
button3.clicked.connect(lambda: button3_click(line1, line2))

layout = QGridLayout()
layout.addWidget(QLabel('批量pdf路径'), 0, 0)
layout.addWidget(line1, 0, 1)
layout.addWidget(button1, 0, 2)

layout.addWidget(QLabel('参考pdf水印'), 1, 0)
layout.addWidget(line2, 1, 1)
layout.addWidget(button2, 1, 2)

layout.addWidget(button3, 3, 0, 1, 3)

win.setLayout(layout)
win.show()
sys.exit(app.exec())