import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl


#Creates a Browser class that inherits from QMainWindow, the main window class for PyQt apps.
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        #Add the Web View
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        # Create Address Bar
        self.address_bar = QLineEdit()
        self.address_bar.setPlaceholderText("Enter URL and press Enter")
        self.address_bar.returnPressed.connect(self.load_url_from_address_bar)

        # Layout to hold the address bar and the browser view
        layout = QVBoxLayout()
        layout.addWidget(self.address_bar)
        layout.addWidget(self.browser)

        # Container widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        #set window properties
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Simple Web Browser')

    def load_url_from_address_bar(self):
        url = QUrl(self.address_bar.text())
        if url.scheme() == "":
            url.setScheme("http")
        self.browser.setUrl(url)




