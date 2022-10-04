# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLabel, QHBoxLayout, QPushButton, QToolTip, QGridLayout, QLCDNumber, QTextEdit, QComboBox, QTableWidget, QSlider
from PyQt5 import Qt, QtCore, QtTest
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QSound


class NPU(QWidget):

    def __init__(self):
        super().__init__()  
        
        self.setWindowTitle('NPU')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.resize(480, 320)

        self.grid = QGridLayout()
        self.grid.setSpacing(5)      
        self.setLayout(self.grid)  


# кнопки "Главная панель"

        self.btn_add_and_settings = QPushButton('Ввод и настройки', self)
        self.btn_add_and_settings.clicked.connect(self.initiate)
        self.grid.addWidget(self.btn_add_and_settings, 1, 0)

        self.btn_change = QPushButton('Изменить', self)
        self.btn_change.setFixedSize(100, 40)
        self.btn_change.clicked.connect(self.change)
        self.grid.addWidget(self.btn_change, 1, 1)

        self.btn_output = QPushButton('Вывод', self)
        self.btn_output.setFixedSize(80, 40)
        self.btn_output.clicked.connect(self.output)
        self.grid.addWidget(self.btn_output, 1, 2)

        self.btn_combo = QComboBox(self)
        self.grid.addWidget(self.btn_combo, 1, 3)

        self.btn_exit = QPushButton('×', self)
        self.btn_exit.setFixedSize(30, 30)
        self.btn_exit.setStyleSheet('background-color: #B52323; color: white')
        self.grid.addWidget(self.btn_exit, 1, 4)
        self.btn_exit.clicked.connect(self.exit_app)


# кнопки "Ввод и настройка"

        self.btn_create_script = QPushButton('Создать сценарий', self)
        self.grid.addWidget(self.btn_create_script, 2, 0)

        self.btn_scripts = QPushButton('Созданные сценарии', self)
        self.btn_scripts.setFont(QFont('Sans Serif', 7))
        self.grid.addWidget(self.btn_scripts, 3, 0)

        self.btn_select_patient = QComboBox(self)
        self.btn_select_patient.setFont(QFont('Sans Serif', 7))
        self.btn_select_patient.addItems(["Выбрать пациента"])
        self.grid.addWidget(self.btn_select_patient, 4, 0)

        self.btn_select_script = QComboBox(self)
        self.btn_select_script.addItems(["Выбрать сценарий"])
        self.btn_select_script.setFont(QFont('Sans Serif', 7))
        self.grid.addWidget(self.btn_select_script, 5, 0)

        self.btn_add_new = QPushButton('Добавить запись', self)
        self.grid.addWidget(self.btn_add_new, 6, 0)

        self.btn_add = QPushButton('Добавить', self)
        self.grid.addWidget(self.btn_add, 6, 3)

        self.table_patients = QTableWidget(0, 3, self)
        self.table_patients.setHorizontalHeaderLabels(["ID", "ФИО", "Возраст"])
        self.table_patients.resizeColumnsToContents()
        self.grid.addWidget(self.table_patients, 2, 1, 4, 4)

        self.btns1 = [self.btn_create_script,
                      self.btn_scripts,
                      self.btn_select_patient,
                      self.btn_select_script,
                      self.btn_add_new,
                      self.btn_add,
                      self.table_patients]

                    
    # кнопки "Измерение"

        self.amplitude = QLabel('Амплитуда тока', self) 
        self.grid.addWidget(self.amplitude, 2, 0, 1, 2)

        self.slider_amp = QSlider(QtCore.Qt.Horizontal, self)
        self.grid.addWidget(self.slider_amp, 3, 0, 1, 2)

        self.lcd = QLCDNumber(self)
        self.slider_amp.valueChanged.connect(self.lcd.display)
        self.lcd.setFixedSize(110, 50)
        self.grid.addWidget(self.lcd, 2, 3, 1, 1)

        self.btn_test_amp = QPushButton('Тест', self)
        self.grid.addWidget(self.btn_test_amp, 3, 3)

        self.btn_select_item = QComboBox(self)
        self.btn_select_item.addItems(["Выбрать запись"])
        self.grid.addWidget(self.btn_select_item, 4, 0)

        self.btn_select_item_detail = QPushButton("Посмотреть сценарии подробнее", self)
        self.btn_select_item_detail.setFont(QFont('Sans Serif', 5))
        self.btn_select_item_detail.setFixedSize(200, 30)
        self.grid.addWidget(self.btn_select_item_detail, 4, 1, 1, 3)

        self.btn_start = QPushButton('Старт', self)
        self.btn_start.setFixedSize(100, 40)
        self.grid.addWidget(self.btn_start, 5, 0)

        self.btn_stop = QPushButton('Стоп', self)
        self.btn_stop.setFixedSize(100, 40)
        self.grid.addWidget(self.btn_stop, 5, 1)
        
        self.btns2 = [self.amplitude,
                      self.slider_amp,
                      self.lcd,
                      self.btn_test_amp,
                      self.btn_select_item,
                      self.btn_select_item_detail,
                      self.btn_start,
                      self.btn_stop]


    # кнопки "Вывод"
        
        self.table_output = QTableWidget(0, 3, self)
        self.table_output.setHorizontalHeaderLabels(["ID", "ФИО/зап.", "Вывод"])
        self.table_output.resizeColumnsToContents()
        self.grid.addWidget(self.table_output, 2, 0, 1, 5)

        self.btns3 = [self.table_output]



        self.show()
        self.initiate()


    def initiate(self): #1
        for i in (self.btns2+self.btns3):
            i.hide() 

        for i in self.btns1:
            i.show() 


    def change(self): #2
        for i in (self.btns1+self.btns3):
            i.hide() 

        for i in self.btns2:
            i.show() 

        
    def output(self): #3
        for i in (self.btns1+self.btns2):
            i.hide()

        self.table_output.show() 


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
    
# P N U N U N P - U N P N P N U  
# QToolTip.setFont(QFont('SansSerif', 50))
        # self.btn_start = QPushButton('Старт', self)
        # self.btn_start.resize(50, 50)
        # self.btn_start.move(100, 100)
        # self.btn_start.setStyleSheet("QPushButton {background-color: #d1d5de; color: black; border-radius: 4px;}"
        #                              "QPushButton:pressed {background-color: #b1b8c7;}")
        # grid.addWidget(self.btn_start, 1, 3)
# self.sound = QSound("whitenoise.wav")

#         self.timer = QtCore.QTimer()
#         self.condition_seq = ['P', 'N', 'U', 'N', 'U', 'N', 'P', 'U', 'N', 'P', 'N', 'P', 'N', 'U']
#         self.condition = 1
# self.btn_start.clicked.connect(self.start)