import sys
from PyQt5.QtWidgets import QApplication

import project.page
import project.bar3d
import project.sunburst

app = QApplication(sys.argv)
mainWindow = project.page.WebPage()
mainWindow.show()
sys.exit(app.exec())