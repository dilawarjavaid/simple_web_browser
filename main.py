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

