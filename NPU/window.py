# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout
from PyQt5 import QtCore


class Window(QWidget):
    '''Основа всех открывающихся окон, отрисовка основных элементов, сетки'''
    
    def __init__(self):
        super().__init__() 

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.resize(480, 320)

        self.grid = QGridLayout()
        self.grid.setSpacing(5)      
        self.setLayout(self.grid)

        self.btn_exit = QPushButton('×', self)
        self.btn_exit.setFixedSize(40, 40)
        self.btn_exit.setStyleSheet('background-color: #B52323; color: white')
        self.grid.addWidget(self.btn_exit, 1, 4)
        
        self.btn_exit.clicked.connect(self.exit_app)
        self.show() 
        self.open_w()


    def exit_app(self):
        sys.exit() 


    def transit(self, cls):
        self.close()
        cls.show()
