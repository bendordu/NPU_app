# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QLabel, QPushButton
from window import Window
from intro import Nine_starl_prob
# from patients import Patients_test
# from start_test import StartTest 
# from sensitive import Sens_test
# from scripts import Script_test


class Check(Window):

    def open_w(self):

        date = QLabel(StartTest.global_date, self) 
        self.grid.addWidget(date, 1, 0)

        patient = QLabel(Patients_test.global_patient, self) 
        self.grid.addWidget(patient, 2, 0)

        sens = QLabel(Sens_test.global_sensetive, self) 
        self.grid.addWidget(sens, 3, 0)

        scr = QLabel(Script_test.global_script, self) 
        self.grid.addWidget(scr, 4, 0)

        btn_start = QPushButton('Начать тест', self)
        btn_start.clicked.connect(self.start)
        self.grid.addWidget(btn_start, 5, 0)

        # btn_start = QPushButton('Проверка датчиков', self)
        # btn_start.clicked.connect(self.start)
        # self.grid.addWidget(btn_start, 6, 0)


    def start(self):
        self.close()
        self.pat = Nine_starl_prob()
        self.pat.show()  