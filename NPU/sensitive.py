# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QLCDNumber, QSlider
from PyQt5 import QtCore
from window import Window
from scripts import Script_test


class SensTest(Window): 
    '''определение чувствительности к электростимуляции'''

    def open_w(self):

        amplitude = QLabel('Амплитуда тока', self) 
        self.grid.addWidget(amplitude, 2, 0, 1, 1)


        self.slider_amp = QSlider(QtCore.Qt.Horizontal, self)
        self.grid.addWidget(self.slider_amp, 3, 0, 1, 2)


        lcd = QLCDNumber(self)
        self.grid.addWidget(lcd, 2, 3, 2, 1)

        self.slider_amp.valueChanged.connect(lcd.display)


        time = QLabel('Время, мс', self) 
        self.grid.addWidget(time, 4, 0, 1, 1)


        self.slider_time = QSlider(QtCore.Qt.Horizontal, self)
        self.grid.addWidget(self.slider_time, 5, 0, 1, 2)


        lcd_time = QLCDNumber(self)
        self.grid.addWidget(lcd_time, 4, 3, 2, 1)

        self.slider_time.valueChanged.connect(lcd_time.display)



        btn_test_amp = QPushButton('Тест', self)
        self.grid.addWidget(btn_test_amp, 6, 0)

        # btn_test_amp.clicked.connect(self.test_amp)


        self.sens()


    # def back_main_window(self):
    #     self.close()
    #     self.back = NPU()
    #     self.back.show()
    # def back_main_window(self):
    #     back_main_window.back_main_window(self)


    # def test_amp(self):
    #     pass


class Sens_main(SensTest):

    def sens(self):

        btn_ok = QPushButton('Назад', self)
        self.grid.addWidget(btn_ok, 6, 1)

        btn_ok.clicked.connect(self.transit(self, NPU()))


class Sens_test(SensTest):

    def sens(self):

        btn_save = QPushButton('OK', self)
        self.grid.addWidget(btn_save, 6, 1)

        btn_save.clicked.connect(self.show_amp)


    def show_amp(self):
        show_amp = QMessageBox()
        show_amp.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        show_amp.setText(str(self.slider_amp.value()) + ' мА, ' + str(self.slider_time.value()) + ' мс')
        show_amp.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        ret = show_amp.exec()
        if ret == QMessageBox.Yes:
            self.sensitive_global = str(self.slider_amp.value()) + ' мА, ' + str(self.slider_time.value()) + ' мс'
            self.transit(self, Script_test())


    def global_sensetive(self):
        return self.sensitive_global


    # def next_to_scr(self):
    #     self.close()
    #     self.scr = Script_test()
    #     self.scr.show()