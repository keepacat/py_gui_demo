from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebChannel import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtNetwork import QNetworkAccessManager,QNetworkRequest

qInstallMessageHandler(lambda *args:None)

class WebPage(QWidget):
    def __init__(self):
        super(WebPage, self).__init__()
        self.initWindow()
        self.initLayout()
        self.initConnect()
        self.initNetwork()

    def initWindow(self):
        self.setGeometry(400, 400, 800, 600)
        self.setWindowTitle("MyWidnow")

        self.frame_web = QFrame()
        self.frame_web.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.frame_web.setVisible(True)

        self.frame_chart = QFrame()
        self.frame_chart.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.frame_chart.setVisible(False)

        self.frame_button = QFrame()
        self.frame_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        
        self.webChannel_web = QWebChannel()
        self.webChannel_web.registerObject("MainWindow", self)

        self.webView_web = QWebEngineView()
        self.webView_web.load(QUrl("http://192.168.10.224:5000/"))
        self.webView_web.page().setWebChannel(self.webChannel_web)

        self.webView_chart = QWebEngineView()
        self.webView_chart.load(QUrl("http://www.baidu.com/"))

        self.pushButton_chart1 = QPushButton()
        self.pushButton_chart1.setText("Button1")

        self.pushButton_chart2 = QPushButton()
        self.pushButton_chart2.setText("Button2")

        self.lineEdit_web = QLineEdit()
        self.lineEdit_web.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

    def initLayout(self):
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.frame_web, 0, 0)
        self.layout.addWidget(self.frame_chart, 0, 1)
        self.layout.addWidget(self.frame_button, 1, 0, 1, 2)

        self.layout = QHBoxLayout(self.frame_web)
        self.layout.addWidget(self.webView_web)
        
        self.layout = QHBoxLayout(self.frame_chart)
        self.layout.addWidget(self.webView_chart)

        self.layout = QHBoxLayout(self.frame_button)
        self.layout.addStretch(0)
        self.layout.addWidget(self.lineEdit_web)
        self.layout.addWidget(self.pushButton_chart1)
        self.layout.addWidget(self.pushButton_chart2)

    def initConnect(self):
        self.pushButton_chart1.clicked.connect(self.on_button1_clicked)
        self.pushButton_chart2.clicked.connect(self.on_button2_clicked)

    def initNetwork(self):
        self.http = QNetworkAccessManager(self)


    @pyqtSlot()
    def on_ReadyRead(self):
        print("on_ReadyRead:")

    @pyqtSlot()
    def on_errorOccurred(self):
        print("on_errorOccurred:")
        
    @pyqtSlot()
    def on_sslErrors(self):
        print("on_sslErrors:")

    @pyqtSlot()
    def on_button1_clicked(self):
        print("hello qt")
        self.webView_web.page().runJavaScript('qtToJsMessage()')

    @pyqtSlot()
    def on_button2_clicked(self):
        get_url = "http://192.168.10.224:5000/"
        get_url += self.lineEdit_web.text()
        print(get_url)    
        reply = self.http.get(QNetworkRequest(QUrl(get_url)))
        reply.readyRead.connect(self.on_ReadyRead)
        reply.errorOccurred.connect(self.on_errorOccurred)
        reply.sslErrors.connect(self.on_sslErrors)




 
