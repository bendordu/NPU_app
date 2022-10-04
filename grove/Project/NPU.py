# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLabel, QHBoxLayout, QPushButton, QToolTip, QGridLayout, QTextEdit, QComboBox, QTableWidget, QToolBar
from PyQt5 import Qt, QtCore, QtTest
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QSound


class NPU(QWidget):

    def __init__(self):
        super().__init__()  
        
        self.setWindowTitle('NPU')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.resize(QApplication.desktop().width(), QApplication.desktop().height())
        self.resize(480, 320)

        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        # # P N U N U N P - U N P N P N U        
        self.setLayout(self.grid)

        self.toolBar = QToolBar()
        self.grid.addWidget(self.toolBar)        

        self.btn_add_and_settings = QPushButton('Ввод и настройки', self)
        self.btn_add_and_settings.setCheckable(True)
        self.btn_add_and_settings.clicked.connect(self.add_and_settings)
        self.toolBar.addWidget(self.btn_add_and_settings)

        #self.btn_change = QPushButton('Изменить', self)
        #self.btn_add_and_settings.setCheckable(True)
        #self.toolBar.addWidget(self.btn_change)

        #self.btn_output = QPushButton('Вывод', self)
        #self.btn_add_and_settings.setCheckable(True)
        #self.toolBar.addWidget(self.btn_output)

        #self.btn_combo = QComboBox(self)
        #self.toolBar.addWidget(self.btn_combo)

        self.btn_exit = QPushButton('×', self)
        self.btn_exit.setFixedSize(50, 50)
        self.btn_exit.setStyleSheet('background-color: #B52323; color: white')
        self.toolBar.addWidget(self.btn_exit)


        self.btn_create_script = QPushButton('Создать сценарий', self)
        self.grid.addWidget(self.btn_create_script, 2, 0)

        self.btn_scripts = QPushButton('Список созданных сценариев', self)
        self.grid.addWidget(self.btn_scripts, 3, 0)

        self.btn_select_patient = QComboBox(self)
        self.grid.addWidget(self.btn_select_patient, 4, 0)

        self.btn_select_script = QComboBox(self)
        self.grid.addWidget(self.btn_select_script, 5, 0)

        self.btn_add_new = QPushButton('Добавить запись', self)
        self.grid.addWidget(self.btn_add_new, 6, 0)

        self.btn_add = QPushButton('Добавить', self)
        self.grid.addWidget(self.btn_add, 6, 3)

        self.table_patients = QTableWidget(0, 3, self)
        self.table_patients.setHorizontalHeaderLabels(["ID", "ФИО", "Возраст"])
        self.table_patients.resizeColumnsToContents()
        self.grid.addWidget(self.table_patients, 2, 1, 4, 3)


        # QToolTip.setFont(QFont('SansSerif', 50))
        # self.btn_start = QPushButton('Старт', self)
        # self.btn_start.resize(50, 50)
        # self.btn_start.move(100, 100)
        # self.btn_start.setStyleSheet("QPushButton {background-color: #d1d5de; color: black; border-radius: 4px;}"
        #                              "QPushButton:pressed {background-color: #b1b8c7;}")
        # grid.addWidget(self.btn_start, 1, 3)

        # self.name_person = QTextEdit(self)
        # self.name_person.move(500, 500)
        # self.name_person.resize(200, 100)
        # self.name_person.setPlaceholderText('Введите имя')

        self.sound = QSound("whitenoise.wav")

        self.timer = QtCore.QTimer()
        self.condition_seq = ['P', 'N', 'U', 'N', 'U', 'N', 'P', 'U', 'N', 'P', 'N', 'P', 'N', 'U']
        self.condition = 1
        
        self.show()
        # self.btn_start.clicked.connect(self.start)
        self.btn_exit.clicked.connect(self.exit_app)


    def add_and_settings(self):
        self.grid.hide()
        self.grid_add_and_settings = QGridLayout()
        self.grid.setSpacing(100)


    def start(self):
        self.text = self.name_person.toPlainText()
        print(self.text)
        for i in range(4):
            self.sound.play()
            self.timer.start(40)
            self.timer.timeout.connect(self.sound.stop)
            QtTest.QTest.qWait(1000)

        while self.condition <= 14:
            if self.condition_seq[self.condition] == 'P':
                for i in range(6):
                    self.sound.play()
                    self.timer.start(40)
                    self.timer.timeout.connect(self.sound.stop)
                    QtTest.QTest.qWait(19960)
                if self.condition == 7:
                    QtTest.QTest.qWait(300000)
                self.condition += 1

            elif self.condition_seq[self.condition] == 'N':
                for i in range(6):
                    self.sound.play()
                    self.timer.start(40)
                    self.timer.timeout.connect(self.sound.stop)
                    QtTest.QTest.qWait(19960)
                self.condition += 1

            elif self.condition_seq[self.condition] == 'U':
                for i in range(6):
                    self.sound.play()
                    self.timer.start(40)
                    self.timer.timeout.connect(self.sound.stop)
                    QtTest.QTest.qWait(19960)
                if self.condition == 14:
                    pass
                else:
                    self.condition += 1    


    def exit_app(self):
        sys.exit() 

                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NPU()
    sys.exit(app.exec_()) 
    