# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import  QLabel, QPushButton
from PyQt5 import QtCore, QtTest
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QSound
from window import Window


class Start_test(Window): #непосредственно сам тест, нужно переделеть, остаются вопросы!!!

    def open_w(self):

        btn_stop = QPushButton('Стоп', self)
        # btn_stop.clicked.connect(self.stop)
        self.grid.addWidget(btn_stop, 1, 0)

        self.number = QLabel('Test', self) 
        self.grid.addWidget(self.number, 3, 1)

        self.sound = QSound("stimuls/whitenoise.wav")
        self.timer = QtCore.QTimer()
        self.condition_seq = ['P', 'N', 'U', 'N', 'U', 'N', 'P']   #, 'U', 'N', 'P', 'N', 'P', 'N', 'U']

        self.green = QPixmap("stimuls/green_circle.png")
        self.red = QPixmap("stimuls/red_square.jpg")
        self.blue = QPixmap("stimuls/blue_triangle.png")

        self.box = QLabel(self)
        # self.box.setPixmap(self.box)
        self.box.setGeometry(120, 80, 200, 200)
        self.box.show()

        self.timer_color = QtCore.QTimer()
        self.timer_color.timeout.connect(self.box.hide)

        self.start()


    def start(self):

        for i in range(4):

            self.sound.play()
            self.timer.start(40)
            self.timer.timeout.connect(self.sound.stop)
            QtTest.QTest.qWait(1000)

        for i in self.condition_seq:

            self.number.hide()
            self.number = QLabel(str(i), self) 
            self.grid.addWidget(self.number, 3, 1)

            if i == 'P':

                for j in range(7)[1:7]:

                    if j//2 == 1:
                        self.timer_color.start(8000)
                        self.box.setPixmap(self.red)
                        self.box.show()

                    self.sound.play()
                    self.timer.start(40)
                    self.timer.timeout.connect(self.sound.stop)
                    QtTest.QTest.qWait(19960)

                self.number.hide()

                # if i == self.condition_seq[6]:
                #     QtTest.QTest.qWait(300000)


            elif i == 'N':

                for j in range(7)[1:7]:

                    if j//2 == 1:
                        self.timer_color.start(8000)
                        self.box.setPixmap(self.green)
                        self.box.show()

                    self.sound.play()
                    self.timer.start(40)
                    self.timer.timeout.connect(self.sound.stop)
                    QtTest.QTest.qWait(19960)

                self.number.hide()


            elif i == 'U':

                for j in range(7)[1:7]:

                    if j//2 == 1:
                        self.timer_color.start(8000)
                        self.box.setPixmap(self.blue)
                        self.box.show()

                    self.sound.play()
                    self.timer.start(40)
                    self.timer.timeout.connect(self.sound.stop)
                    QtTest.QTest.qWait(19960)

                self.number.hide()

                # if i == self.condition_seq[14]:
                #     pass  