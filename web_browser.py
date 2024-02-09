from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MyWebBrowser(QMainWindow):

    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("Faiz Khan Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.search_btn = QPushButton("Seacrh")
        self.search_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">>")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.search_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        self.search_btn.clicked.connect(
            lambda: self.url_navigate(self.url_bar.toPlainText())
        )
        self.search_btn.clicked.connect(self.browser.back)
        self.search_btn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://faizkhanpy.pythonanywhere.com/"))

        self.window.setLayout(self.layout)
        self.window.show()

    def url_navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))


web = QApplication([])
window = MyWebBrowser()
web.exec_()
