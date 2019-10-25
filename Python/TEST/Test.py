# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lami/Desktop/未命名檔案夾/TEST.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

qtCreatorFile ＝"/Users/lami/Desktop/未命名檔案夾/TEST.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MainUi(QtWidgets.QMainWindow, Ui_MainWindow):  # Python的多重繼承 MainUi 繼承自兩個類別
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


from mainForm import MainUi   # 讀入我們設計的Main Window
import sys
    
if __name__ == "__main__":
    def run_app():
        app = QtWidgets.QApplication(sys.argv)
        window = MainUi()
        window.show()
        app.exec_()
    run_app()