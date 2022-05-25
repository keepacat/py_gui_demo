from PyPDF2 import PdfFileReader, PdfFileWriter
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

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

if __name__ == '__main__':
    app = QApplication(sys.argv)

    files = QFileDialog.getOpenFileNames()[0]
    markfile = QFileDialog.getOpenFileName()[0]

    for file in files:
        pdf_file_in = file
        pdf_file_mark = markfile
        pdf_file_out = file.replace('.pdf', '_Marked.pdf')
        add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)
    