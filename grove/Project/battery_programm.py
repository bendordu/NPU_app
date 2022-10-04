# -*- coding: utf-8 -*-
import sys
import battery_check
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLabel, QHBoxLayout, QPushButton, QToolTip, QGridLayout, QTextEdit, QComboBox, QTableWidget, QToolBar
from PyQt5 import Qt, QtCore, QtTest
from PyQt5.QtGui import QFont

class battery(QWidget):

    def __init__(self):
        super().__init__()  
        
        self.setWindowTitle('Battery_check')
        #self.QLabel('Data', self)
    
    def check():
        battery_data=battery_check.check()
        for i in battery_data:
            L1 = QLabel(i)
            show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = battery.check()
    sys.exit(app.exec_()) 