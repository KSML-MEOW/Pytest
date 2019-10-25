#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:37:10 2019

@author: lami
"""

from PyQt5 import QtWidgets, uic
import os


path = os.getcwd()

qtCreatorFile = path + os.sep + "ui" + os.sep + "TEST.ui"  # 設計好的ui檔案路徑
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)   # 讀入用Qt Designer設計的GUI layout


#In []
class MainUi(QtWidgets.QDialog, Ui_MainWindow):  # Python的多重繼承 MainUi 繼承自兩個類別
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)