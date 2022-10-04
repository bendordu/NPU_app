# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMessageBox, QCalendarWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from window import Window
# from patients import Patients_test


class StartTest(Window):

    def open_w(self):

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.setFont(QFont('Sans Serif', 5))
        cal.clicked[QtCore.QDate].connect(self.showDate)
        self.grid.addWidget(cal, 2, 0, 6, 5)


    def showDate(self, date):
        showDate = QMessageBox()
        showDate.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        showDate.setText(date.toString()+', верно?')
        showDate.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        ret = showDate.exec()
        if ret == QMessageBox.Yes:
            self.date_global = date.toString()
            self.transit(self, Patients_test())


    def global_date(self):
        return self.date_global
        

     


